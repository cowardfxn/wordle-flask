#!/bin/python
# encoding: utf-8

import random
import os
import numpy as np
from datetime import datetime

random.seed(datetime.now().timestamp())


def get_words():
    with open(
        os.path.join(os.path.dirname(__file__), "wrods_5.txt"), "r", encoding="utf-8"
    ) as ifs:
        words = [w.strip() for w in ifs]

    return words


o_words = get_words()


def get_random_words(words, size=5):
    randoms = set()
    while len(randoms) < size and len(randoms) != len(words):
        randoms.add(random.choice(words))
    return list(randoms)


def random_guess(words=o_words, str_correct=" " * 5, str_ng="", w_wrong="", size=5):
    w_correct = list(str_correct)
    w_ng = list(str_ng)
    if str_correct == " " * 5 and not w_wrong or not w_ng:
        return get_random_words(words, size)

    possible_words = []
    nw_idx = 0
    while len(possible_words) < size * 10 and nw_idx < len(words) * 1000:
        new_word = words[nw_idx % len(words)]
        nw_idx += 100
        valid = True
        if new_word in possible_words:
            continue
        for w in w_ng:
            if w in new_word and w not in w_correct:
                valid = False
                break

        if valid:
            for i_ng in range(5):
                if w_wrong[i_ng]:
                    if new_word[i_ng] in w_wrong[i_ng]:
                        valid = False
                        break

                    for w in w_wrong[i_ng]:
                        if w not in new_word:
                            valid = False
                            break

        if valid:
            for idx, w in enumerate(w_correct):
                if w != " " and new_word[idx] != w:
                    valid = False
                    break

        if valid:
            possible_words.append(new_word)
            if len(possible_words) == size * 10:
                break

    random_words = []
    if possible_words:
        random_words = get_random_words(possible_words, size)
        random_words.sort()
    return random_words


if __name__ == "__main__":
    # word in the correct spot
    # w_correct = " " * 5
    w_correct = " r   "

    # word in the wrong spot
    w_wrong = ("a", "", "", "", "")

    # not the word
    w_ng = "gil"

    print(random_guess(o_words, w_correct, w_ng, w_wrong, 10))
