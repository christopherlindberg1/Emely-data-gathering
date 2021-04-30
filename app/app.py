from flask import Flask, render_template, request, flash, redirect, url_for, session

import os
from pathlib import Path

from data_access.text_file_reader import TextFileReader
from core_functionality.question_generator import QuestionGenerator
from forms.dialogue import Dialogue




app = Flask(__name__)

text_file_reader = TextFileReader()
question_generator = QuestionGenerator()

@app.route("/")
def index():
    """ Returns the landing page """

    form = Dialogue(request.form)
    question = question_generator.get_random_question()

    return render_template("index.html", form = form, question = question)


if __name__ == "__main__":
    app.run(debug=True)