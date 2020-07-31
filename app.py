# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import morse


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/results', methods=['GET', 'POST'])
def results():
    morseMsg = request.form["input"]
    pants = morse(morseMsg)
    return render_template("results.html", morseMsg=morseMsg, pants=pants)