# learn python packages
# when init is used, python treats the directory as a package

from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("/public/index.html")

@app.route("/jinja")
def jinja():

    my_name = "Zahin"
    age=30
    langs=["Python", "Javascript", "C", "C++", "Java"]

    friends = {
        "Nazim": 30,
        "Kashem": 28,
        "Konstantin": 26,
        "Ahmed": 27
    }
    return render_template("/public/jinja.html", my_name=my_name)

@app.route("/about")
def about():
    return render_template("/public/about.html")