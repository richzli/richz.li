from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/sitedb"
mongo = PyMongo(app)

from app import routes, blog

app.register_blueprint(blog.blog, url_prefix="/blog")