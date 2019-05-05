from flask import Flask, render_template, redirect, url_for, request, session
import pyrebase
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", navbarchoice="first", footer=False)


if __name__ == '__main__':
    app.run()
