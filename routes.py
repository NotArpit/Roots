from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home ():
	return render_template("home.html")

@app.route("/<id>")
def profile(id):

	return render_template("profile.html", id = id)