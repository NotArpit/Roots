from flask import Flask, render_template, url_for, redirect
from foodSystem import *
from user import *
from server import app, system, userA, userB
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/<int:id>")
def index(id):
	return render_template("index.html", id = id)

@app.route("/trade/<id>", methods=["GET", "POST"])
def trade(id):
    #date, place, food
    if request.method == "POST":
        # updating the quantities of each food
        counter = 1
        while counter <= details.n_food:
            buffer = "food"
            buffer += counter
            request.form.get('')
            counter += 1
        

    return render_template("trade.html", details = details)

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

        return redirect("{{url_for('index')}}")
 
    return render_template("addTrade.html", id=id)
