# learn python packages
# when init is used, python treats the directory as a package

from app import app
from flask import render_template
from datetime import datetime

from app import app


@app.template_filter("clean_date")
def clean_date(dt):
    return


@app.route("/")
def index():
    return render_template("/public/index.html")


@app.route("/jinja")
def jinja():

    my_name = "Zahin"
    age = 30
    langs = ["Python", "Javascript", "C", "C++", "Java"]

    friends = {
        "Nazim": 30,
        "Kashem": 28,
        "Konstantin": 26,
        "Ahmed": 28
    }

    colours = ("Red", "Green")

    cool = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f"Pulling repo {self.name}"

        def clone(self):
            return f"Cloning into {self.url}"

        def __str__(self):
            return f"self.name"

    def repeat(x, qty):
        return x*qty

    my_remote = GitRemote(name="Flask Jinja",
                          description="Template design tutorial",
                          url="https://github.com/julian-nash/jinja.git"


                          )

    print(my_remote)
    return render_template("/public/jinja.html", my_name=my_name, age=age, langs=langs, friends=friends, colours=colours, cool=cool, GitRemote=GitRemote, repeat=repeat, my_remote=my_remote)


@ app.route("/about")
def about():
    return render_template("/public/about.html")
