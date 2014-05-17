from flask import render_template, flash, redirect, request, url_for
from wedding import app


@app.route('/index')
def index():
    return render_template("index.html")