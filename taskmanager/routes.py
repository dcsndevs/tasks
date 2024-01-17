from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, db

@app.route("/")
def home():
    return render_template("base.html")
