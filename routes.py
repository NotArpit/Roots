from flask import Flask, render_template, url_for, redirect
from foodSystem import *
from user import *
from server import *
from flask import Flask, render_template, url_for, redirect, request
from trade import *


bananaQ = 200
strawberriesQ = 223


@app.route("/<int:id>")
def index(id):
	return render_template("index.html", id = id)

@app.route("/addTrade/<int:id>", methods=["GET","POST"])
def addTrade(id):
	return render_template("addTrade.html", id=id)

@app.route("/listing/<int:id>", methods=["GET","POST"])
def listing(id):
	bananaQ = 200
	strawberriesQ = 223

	if request.method == "POST":
		quantityH = request.form["quantity1"]
		print(quantityH)
		quantityW = request.form["quantity2"]
		print(quantityW)
		bananaQ = bananaQ - int(str(quantityW))
		strawberriesQ = strawberriesQ - int(str(quantityH))

		return render_template("listing.html", strawberriesQ=strawberriesQ, bananaQ=bananaQ, id=id)
	else:
		return render_template("listing.html", strawberriesQ = strawberriesQ, bananaQ =bananaQ, id=id)
