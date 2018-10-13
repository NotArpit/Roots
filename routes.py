from flask import Flask, render_template, url_for, redirect
from foodSystem import *
from user import *
from server import app, system

@app.route("/")
def home ():
	return render_template("home.html")

@app.route("/<id>")
def profile(id):

	return render_template("profile.html", id = id)