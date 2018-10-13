from flask import Flask, render_template, url_for, redirect
from foodSystem import *
from user import *
from server import *
from flask import Flask, render_template, url_for, redirect, request
from trade import *

@app.route("/<int:id>")
def index(id):
	return render_template("index.html", id = id)

@app.route("/addTrade/<int:id>", methods=["GET","POST"])
def addTrade(id):
    if request.method == "POST":
        #This is to do with the title
        trade_title = request.form["title"]
        #This is to do with what you have:
        product_have = request.form["productH"]
        quantity_have = request.form["quantityH"]
        #This is to do with what you want:
        product_want = request.form["productW"]
        quantity_want = request.form["quantityW"]

        return redirect("{{url_for('index')}}", title = trade_title, p_have = product_have,
            q_have = quantity_have, p_want = product_want, q_want = quantityW)

@app.route("/listing/<int:id>", methods=["GET","POST"])
def listing(id):
    return render_template("listing.html", id=id)
