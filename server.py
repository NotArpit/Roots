from flask import Flask 
from foodSystem import *
from user import *
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Another_highly_secret_key'


system = foodSystem()
userA = User()
userB = User()

# csv reader for price list
with open('foodList.csv', 'r') as csvfile:
    foodReader = csv.reader(csvfile)
    # row 1: food name, row2: food price
    for row in foodReader:
    	system.addPriceList(row[0], row[1])

# csv reader for foodWant - Person A
with open('foodWantA.csv', 'r') as csvfile:
    foodReader = csv.reader(csvfile)
    for row in foodReader:
    	# row 1: food name, row2: food quantity
        userA.addFruitW(row[0], row[1])

# csv reader for foodhave- Person A
with open('foodHaveA.csv', 'r') as csvfile:
	foodReader = csv.reader(csvfile)
	for row in foodReader:
		userA.addFruitH(row[0],row[1])

# csv reader for foodWant - Person B
with open('foodWantB.csv', 'r') as csvfile:
	foodReader = csv.reader(csvfile)
	for row in foodReader:
		userB.addFruitW(row[0], row[1])

# csv reader for foodHave - Person B
with open('foodHaveB.csv', 'r') as csvfile:
	foodReader = csv.reader(csvfile)
	for row in foodReader:
		userB.addFruitH(row[0], row[1])