from flask import Flask, render_template, url_for, redirect
from foodSystem import *
from user import *
from server import app, system, userA, userB
from flask import Flask, render_template, url_for, redirect, request
from trade import *

@app.route("/<int:id>")
def index(id):
	return render_template("index.html", id = id)

@app.route("/addTrade/<int:id>", methods=["GET","POST"])
def addTrade(id):
    if request.method == "POST":
    	
    return render_template("addTrade.html", id=id)
