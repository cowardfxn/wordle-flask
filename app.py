#!/bin/python
# encoding: utf-8

import json
from flask import Flask, render_template, request, redirect, url_for
from wordle import random_guess

app = Flask(__name__)


@app.get("/")
def start_up():
    return render_template(
        "index.html", **{"words": random_guess(), "correct": " " * 5}
    )


@app.post("/guess")
def guess_word():
    form = request.form
    str_correct = ""
    w_wrong = [""] * 5
    str_ng = ""
    for i in range(5):
        str_correct += form.get(f"c{i}", " ") or " "
        w_wrong[i] += form.get(f"w{i}", "")
    str_ng += form.get("ng", "")
    guesses = random_guess(
        str_correct=str_correct, w_wrong=w_wrong, str_ng=str_ng, size=10
    )
    return render_template(
        "index.html",
        **{
            "words": guesses,
            "correct": str_correct,
            "wrong": w_wrong,
            "not_words": str_ng.strip(),
        },
    )


if __name__ == "__main__":
    port = 4321
    app.run("0.0.0.0", port, debug=True)
    print(f"App running at http://localhost:{port}")
