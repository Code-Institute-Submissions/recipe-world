import os
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "recipeworlddb"
app.config["MONGO_URI"] = "mongodb://krivan.peter:jel123szo@ds149122.mlab.com:49122/recipeworlddb"

mongo = PyMongo(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",
    foods=mongo.db.foods.find())

@app.route("/breakfasts")
def get_breakfasts():
    return render_template("index.html", 
    foods=mongo.db.foods.find({"category_name": "breakfast"}), title="Breakfasts")

@app.route("/mains")
def get_mains():
    return render_template("index.html", 
    foods=mongo.db.foods.find({"category_name": "main"}), title="Mains")
    
@app.route("/desserts")
def get_desserts():
    return render_template("index.html", 
    foods=mongo.db.foods.find({"category_name": "dessert"}), title="Desserts")
    
@app.route('/<food_name>')
def get_food(food_name):
    return render_template("food.html", 
    food=mongo.db.foods.find_one({"name": food_name}))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)