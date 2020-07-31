from flask import render_template
from app import app

pages = ("about", "projects", "blog", "contact")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html", title = "about", nav = pages)

@app.route("/projects")
def projects():
    return render_template("projects.html", title = "projects", nav = pages)

@app.route("/projects/<name>")
def project_view(name):
    return render_template("projects.html", title = name, nav = pages)

@app.route("/blog")
def blog():
    return render_template("blog.html", title = "blog", nav = pages)

@app.route("/contact")
def contact():
    return render_template("contact.html", title = "contact", nav = pages)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title = "404")
