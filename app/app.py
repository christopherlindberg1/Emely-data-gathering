from flask import Flask, render_template, request, flash, redirect, url_for, session

import os
from pathlib import Path, PurePath
import sys
sys.path.append("../")  # Needed to access config file outside of repo

import config
from core_functionality.dialogue_saver import DialogueSaver
from core_functionality.question_generator import QuestionGenerator

from forms.dialogue import Dialogue


app = Flask(__name__)
app.config["SECRET_KEY"] = config.secret_key


question_generator = QuestionGenerator()
dialogue_saver = DialogueSaver()


@app.route("/")
def index():
    """ Returns the landing page """

    form = Dialogue(request.form)
    base_question = question_generator.get_random_base_question()
    session["base_question"] = base_question

    return render_template("index.html", form = form, base_question = base_question)


@app.route("/submit-dialogue/", methods = ["POST"])
def submit_dialogue():
    """ Saves the user generated data to a text file """

    form = Dialogue(request.form)

    if form.validate() == False:
        flash("You dialogue was not submitted correctly", "danger")
        return redirect(url_for("index"))
    
    base_question = session["base_question"]
    a_one = request.form["user_answer_one"]
    f_one = request.form["user_follow_up_one"]
    a_two = request.form["user_answer_two"]
    f_two = request.form["user_follow_up_two"]

    dialogue_saver.save_dialogue(base_question, a_one, f_one, a_two, f_two)
    
    session["base_question"] = None
    
    return redirect(url_for("thank_you"))


@app.route("/thank-you/")
def thank_you():
    return render_template("thank-you.html")


@app.route("/about/")
def about():
    return render_template("about.html")
        

if __name__ == "__main__":
    app.run(debug = True)