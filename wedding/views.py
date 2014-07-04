from flask import render_template
from wedding import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/template')
def index_template():
    return render_template("index_template.html")