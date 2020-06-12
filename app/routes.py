from flask import render_template
from app import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html", title = "about", nav = True)

@app.route("/projects")
def projects():
    return render_template("projects.html", title = "projects", nav = True)

@app.route("/blog")
def blog():
    return render_template("blog.html", title = "blog", nav = True)

@app.route("/contact")
def contact():
    return render_template("contact.html", title = "contact", nav = True)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title = "404")