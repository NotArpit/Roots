from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route("/<int:id>")
def index(id):
	return render_template("index.html", id = id)

@app.route("/trade/<id>", methods=["GET", "POST"])
def trade(id):
    # query all the deatils of this trade
    details = Trades.query.filter_by(id=id).first()

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
        #logic here
        pass
    return render_template("addTrade.html", id=id)

@app.route("/listing/<int:id>", methods=["GET","POST"])
def listing(id):
    if request.method == "POST":
        pass
    return render_template("listing.html", id=id)
