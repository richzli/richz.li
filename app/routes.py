from flask import render_template, render_template_string, abort
from app import app, mongo, render
import json, os, time

DATA_FILENAME = "./data/data.json"
data = {}
last_updated = 0

@app.before_request
def update_data():
    global data, last_updated
    curr_time = os.path.getmtime(DATA_FILENAME)
    if curr_time > last_updated:
        f = open(DATA_FILENAME, "r")
        data = json.load(f)
        f.close()
        last_updated = curr_time

update_data()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html", title = "about", nav = data["pages"])

@app.route("/projects")
def projects():
    return render_template("projects.html", title = "projects", nav = data["pages"], projects = data["projects"])

@app.route("/projects/<link>")
def project_view(link):
    #try:
    content = open(f"./data/projects/{link}.md", "r").read()
    print("DONE!")
    a = render.render_project_page(content)
    print(a)
    return render_template_string(render.render_project_page(content), title = link, nav = data["pages"])
    #except:
    #    abort(404)

@app.route("/blog")
def blog():
    return render_template("blog.html", title = "blog", nav = data["pages"])

@app.route("/contact")
def contact():
    return render_template("contact.html", title = "contact", nav = data["pages"])

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title = "404")
