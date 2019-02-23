import os
from flask import Flask, render_template, redirect, url_for, request, session, json, jsonify, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename

UPLOAD_FOLDER ="static/user_images"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.secret_key = "ran1dom2string3"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config["MONGO_DBNAME"] = "recipeworlddb"
app.config["MONGO_URI"] = "mongodb://krivan.peter:jel123szo@ds149122.mlab.com:49122/recipeworlddb"

mongo = PyMongo(app)

@app.route("/")
@app.route("/index")
def index():
    foods=mongo.db.foods.find()
    if "username" in session:
        return render_template("index.html", foods=foods, username=session["username"])   
    return render_template("index.html", foods=foods)

@app.route("/breakfasts")
def get_breakfasts():
    foods=mongo.db.foods.find({"category_name": "breakfast"})
    if "username" in session:
        return render_template("index.html", foods=foods, title="Breakfasts", username=session["username"])
    return render_template("index.html", foods=foods, title="Breakfasts")

@app.route("/mains")
def get_mains():
    foods=mongo.db.foods.find({"category_name": "main"})
    if "username" in session:
        return render_template("index.html", foods=foods, title="Mains", username=session["username"])
    return render_template("index.html", foods=foods, title="Mains")
    
@app.route("/desserts")
def get_desserts():
    foods=mongo.db.foods.find({"category_name": "dessert"})
    if "username" in session:
        return render_template("index.html", foods=foods, title="Desserts", username=session["username"])    
    return render_template("index.html", foods=foods, title="Desserts")
    
@app.route("/<food_name>")
def get_food(food_name):
    food=mongo.db.foods.find_one({"name": food_name})
    if "username" in session:
        return render_template("food.html", food=food, username=session["username"])    
    return render_template("food.html", food=food)

@app.route("/sign_up", methods=['POST'])
def sign_up():
    exist = ""
    username =  request.form["username"];
    session["username"] = username
    email = request.form["email"];
    if mongo.db.users.find({"username": username}).count() >= 1 and mongo.db.users.find({"email": email}).count() == 0:
        exist = "username_exists"
        return exist
    elif mongo.db.users.find({"email": email}).count() >= 1 and mongo.db.users.find({"username": username}).count() == 0:
        exist = "email_exists"
        return exist
    elif mongo.db.users.find({"email": email}).count() >= 1 and mongo.db.users.find({"username": username}).count() >= 1:
        exist = "email_and_username_exist"
        return exist
    else:
        mongo.db.users.insert({ "username": username , "email": email, "favorites": "" })
        foods=mongo.db.foods.find()
        return render_template("index.html", foods=foods, username=session["username"])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file():
    file = request.files['picInput']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        pic_url = ""
        return pic_url
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        pic_url = "static/user_images/" + filename
        return pic_url
    pic_url = ""
    return pic_url

@app.route("/new_recipe", methods=["GET", "POST"])
def new_recipe():
    username = session["username"]
    foods=mongo.db.foods.find()
    if request.method == "POST":
        foodname = request.form["foodname"].lower()
        category_name = request.form["categoryselect"].lower()
        author = request.form["author"]
        description = request.form["shortdesc"].lower()
        
        ingredients1 = request.form["ingredients1"]
        ingredients2 = request.form.getlist("ingredients2")
        ingredients2.insert(0, ingredients1)
        
        method1 = request.form["method1"]
        method2 = request.form.getlist("method2")
        method2.insert(0, method1)
        
        pic_url = ""
        pic_url = upload_file()
        
        food = dict(
            category_name = category_name,
            name = foodname,
            author = author,
            pic_url = pic_url,
            likes = 0,
            favorites = 0,
            description = description,
            ingredients = ingredients2,
            method = method2
            )
        mongo.db.foods.insert(food)
        food=mongo.db.foods.find_one({"name": foodname})
        return render_template("food.html", food=food, username=session["username"]) 
    return render_template("newrecipe.html", username = username)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)