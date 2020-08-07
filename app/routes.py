from flask import render_template, abort
from app import app
import json

f = open("./app/data.json", "r")
data = json.load(f)
pages = data["pages"]
f.close()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html", title = "about", nav = pages)

@app.route("/projects")
def projects():
    return render_template("projects.html", title = "projects", nav = pages, projects = data["projects"])

@app.route("/projects/<name>")
def project_view(name):
    try:
        return render_template(f"projects/{name}.html", title = name, nav = pages)
    except:
        abort(404)

@app.route("/blog")
def blog():
    return render_template("blog.html", title = "blog", nav = pages)

@app.route("/contact")
def contact():
    return render_template("contact.html", title = "contact", nav = pages)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title = "404")
