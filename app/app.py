from flask import Flask, render_template, request, flash, redirect, url_for, session


app = Flask(__name__)

@app.route("/")
def index():
    """ Returns the landing page """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)