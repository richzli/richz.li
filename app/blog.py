from flask import Blueprint, render_template, abort
from app import mongo
from app.routes import data

blog = Blueprint("blog", __name__, template_folder="templates")

@blog.route("")
def index():
    return render_template("blog.html", title = "blog", nav = data["pages"])