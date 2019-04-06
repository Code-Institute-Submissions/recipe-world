import os, sys
from flask import Flask, render_template, redirect, url_for, request, session, json, jsonify, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename
from operator import itemgetter


UPLOAD_FOLDER ="static/user_images"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.secret_key = "ran1dom2string3"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

app.config["MONGO_DBNAME"] = "recipeworlddb"
app.config["MONGO_URI"] = "mongodb://krivan.peter:jel123szo@ds149122.mlab.com:49122/recipeworlddb"

mongo = PyMongo(app)

@app.route("/")
@app.route("/index")
def index():
    cuisines=mongo.db.cuisines.find()
    foods = mongo.db.foods.find().sort("favorites", -1)
    meals = mongo.db.foods.find().sort("favorites", -1)
    if "username" in session:
        return render_template("index.html", cuisines=cuisines, foods=foods, meals=meals, username=session["username"])   
    return render_template("index.html", cuisines=cuisines, foods=foods, meals=meals)
    
def food_collect(title, foods, meals):
    if "username" in session:
        return render_template("index.html", foods=foods, meals=meals, title=title, username=session["username"])   
    else:
        return render_template("index.html", foods=foods, meals=meals, title=title)

@app.route("/breakfasts")
def get_breakfasts():
    foods=mongo.db.foods.find({"mealtype_name": "breakfast"}).sort("favorites", -1)
    meals=mongo.db.foods.find({"mealtype_name": "breakfast"}).sort("favorites", -1)
    return food_collect("Breakfasts", foods, meals)

@app.route("/mains")
def get_mains():
    foods=mongo.db.foods.find({"mealtype_name": "main"}).sort("favorites", -1)
    meals=mongo.db.foods.find({"mealtype_name": "main"}).sort("favorites", -1)
    return food_collect("Mains", foods, meals)
    
@app.route("/desserts")
def get_desserts():
    foods=mongo.db.foods.find({"mealtype_name": "dessert"}).sort("favorites", -1)
    meals=mongo.db.foods.find({"mealtype_name": "dessert"}).sort("favorites", -1)
    return food_collect("Desserts", foods, meals)
    
@app.route("/<food_name>")
def get_food(food_name):
    food=mongo.db.foods.find_one({"name": food_name})
    if "username" in session:
        return render_template("food.html", food=food, username=session["username"])    
    else:
        return render_template("food.html", food=food)

@app.route("/cuisine/<cuis_name>")
def get_cuis(cuis_name):
    foods=sorted(mongo.db.foods.find({"cuisine_name": cuis_name}),key=itemgetter('favorites'), reverse=True)
    meals=sorted(mongo.db.foods.find({"cuisine_name": cuis_name}),key=itemgetter('favorites'), reverse=True)
    return food_collect(cuis_name, foods, meals)

@app.route("/my_recipes")
def get_my_recipes():
    recipe_page = True
    my_recipe = True
    username = session["username"]
    if mongo.db.foods.find({"uploaded_by": username}).count() < 1:
        return render_template("index.html", title="My Recipes", recipe_page=recipe_page, username=username)
    else:
        foods=mongo.db.foods.find({"uploaded_by": username})
        meals=mongo.db.foods.find({"uploaded_by": username})
        if "username" in session:
            return render_template("index.html", foods=foods, meals=meals, title="My recipes", my_recipe=my_recipe, username=session["username"])   
        else:
            return render_template("index.html", foods=foods, meals=meals, title="My recipes", my_recipe=my_recipe)

@app.route("/my_favorites")
def get_my_favorites():
    favorite_page = True
    username = session["username"]
    if mongo.db.foods.find({"favorites": username}).count() < 1:
        return render_template("index.html", title="My Favorites", favorite_page=favorite_page, username=username)
    else:
        foods=mongo.db.foods.find({"favorites": username})
        meals=mongo.db.foods.find({"favorites": username})
        return food_collect("My Favorites", foods, meals)

@app.route("/sign_up", methods=["POST"])
def sign_up():
    exist = ""
    session["username"] = request.form["username"];
    username = session["username"]
    email = request.form["email"];
    mongo.db.users.create_index([("username", "text")])
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
        mongo.db.users.insert({ "username": username , "email": email, "favorites": [], "my_recipes":[] })
        foods=mongo.db.foods.find()
        return index()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(foodid):
    try:
        file = request.files['picInput']
        if file.filename == '':
            pic_url = "static/images/no_pic.png"
            return pic_url
        elif file and allowed_file(file.filename):
            filename_split = file.filename.rsplit(".", 1)
            file_name = str(foodid) + "."
            fileformat = filename_split[1]
            filename = secure_filename(file_name + fileformat)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            pic_url = "static/user_images/" + filename
            return pic_url
        else:
            pic_url = "static/images/no_pic.png"
            return pic_url
    except:
        pic_url = "static/images/no_pic.png"
        return pic_url
        
        
@app.route("/edit_recipe/<food_id>", methods=["GET", "POST"])
def edit_recipe(food_id):
    username = session["username"]
    food_id = food_id
    food = mongo.db.foods.find_one({"_id" : ObjectId(food_id)})
    if request.method == "POST":
        foodname = request.form["foodname"].lower()
        mealtype_name = request.form["mealtypeselect"].lower()
        cuisine_name = request.form["cuisineselect"].lower()
        author = request.form["author"]
        description = request.form["shortdesc"].lower()
        
        ingredients1 = request.form.getlist('ingredients1')
        ingredients2 = request.form.getlist('ingredients2')
        
        ingredients1.reverse()
        for elem in ingredients1:
            ingredients2.insert(0, elem)
        
        method1 = request.form.getlist('method1')
        method2 = request.form.getlist('method2')
        method1.reverse()
        for elem in method1:
            method2.insert(0, elem)
        cuisine = mongo.db.cuisines.find_one({"foods" : ObjectId(food_id)})
        searched_cuisine = cuisine["cuisine_name"]
        if searched_cuisine != cuisine_name:
            mongo.db.cuisines.update_one({"foods" : ObjectId(food_id)},
                                        {"$pull" : {"foods" : ObjectId(food_id)}})
            mongo.db.cuisines.update_one({"cuisine_name": cuisine_name},
                                        {"$push": {"foods": ObjectId(food_id)}})
                                        
        mongo.db.foods.update_one(  {"_id" : ObjectId(food_id)},
                                    {"$set": {
                                        "name": foodname,
                                        "mealtype_name": mealtype_name,
                                        "author": author,
                                        "cuisine_name": cuisine_name,
                                        "description": description,
                                        "ingredients": ingredients2,
                                        "method": method2}})
        return get_my_recipes() 
    mealtypes = mongo.db.mealtypes.find()
    cuisines = mongo.db.cuisines.find()
    return render_template("newrecipe.html", food = food, mealtypes=mealtypes, cuisines=cuisines, username=username)

@app.route("/new_recipe", methods=["GET", "POST"])
def new_recipe():
    username = session["username"]
    mealtypes = mongo.db.mealtypes.find()
    cuisines = mongo.db.cuisines.find()
    if request.method == "POST":
        foodname = request.form["foodname"].lower()
        mealtype_name = request.form["mealtypeselect"].lower()
        cuisine_name = request.form["cuisineselect"].lower()
        author = request.form["author"]
        description = request.form["shortdesc"].lower()
        
        ingredients1 = request.form["ingredients1"]
        ingredients2 = request.form.getlist("ingredients2")
        ingredients2.insert(0, ingredients1)
        
        method1 = request.form["method1"]
        method2 = request.form.getlist("method2")
        method2.insert(0, method1)
        
        uploaded_by = username
        food = dict(
            mealtype_name = mealtype_name,
            name = foodname,
            author = author,
            uploaded_by = uploaded_by,
            cuisine_name = cuisine_name,
            favorites = [],
            description = description,
            ingredients = ingredients2,
            method = method2
            )
        mongo.db.foods.insert(food)
        uploaded_food = mongo.db.foods.find(food)
        for element in uploaded_food:
            foodid = element["_id"]
        pic_url = upload_file(foodid)
        mongo.db.foods.update_one({"_id": ObjectId(foodid)}, {"$set": {"pic_url": pic_url}})
        mongo.db.users.update_one({"username": username}, {"$push": {"my_recipes": foodid}})
        mongo.db.cuisines.update_one({"cuisine_name": cuisine_name}, {"$push": {"foods": ObjectId(foodid)}})
        foods=mongo.db.foods.find({"uploaded_by": username})
        return get_my_recipes()
    return render_template("newrecipe.html", mealtypes=mealtypes, cuisines=cuisines, username=username)
    
@app.route("/search_for", methods=["POST"])
def search_for():
    no_results = True
    search_text = request.form["search_text"];
    if mongo.db.foods.find({"$text": {"$search": search_text}}).limit(10).count() < 1:
        if "username" in session:
            return render_template("index.html", title="The results of your search", no_results=no_results, username=session["username"])
        else:
            return render_template("index.html", title="The results of your search", no_results=no_results)
    else:
        foods = mongo.db.foods.find({"$text": {"$search": search_text}}).limit(10)
        meals = mongo.db.foods.find({"$text": {"$search": search_text}}).limit(10)
        return food_collect("The results of your search", foods, meals)

@app.route("/sign_out")
def sign_out():
    session.pop('username', None)
    return index()
 
@app.route("/check_favorites", methods=["GET"])
def check_favorites():
    favorites_exist = ""
    if "username" in session:
        username = session["username"]
        foodid = request.args.get('foodid', None)
        userdb = mongo.db.users.find({"$and":[{"username":username}, { "favorites": foodid }]}).count()
        if userdb >= 1:
            favorites_exist = "favorites_exist"
            return favorites_exist
        else:
            favorites_exist = ""
            return favorites_exist
    else:
        favorites_exist = "no_user"
        return favorites_exist

@app.route("/add_favorites", methods=["GET"])
def add_favorites():
    favorites_exist = ""
    if "username" in session:
        username = session["username"]
        foodid = request.args.get('foodid', None)
        userdb = mongo.db.users.find({"$and":[{"username":username}, { "favorites": foodid }]}).count()
        if userdb >= 1:
            mongo.db.users.update_one({"username": username}, {"$pull": {"favorites": foodid}})
            mongo.db.foods.update_one({"_id" : ObjectId(foodid)}, {"$pull": {"favorites": username}})
            food = mongo.db.foods.find({"_id" : ObjectId(foodid)})
            for element in food:
                number_of_favorites = len(element["favorites"])
                favorites_exist = "favorites" + str(number_of_favorites)
        else:
            mongo.db.users.update_one({"username": username}, {"$push": {"favorites": foodid}})
            mongo.db.foods.update_one({"_id" : ObjectId(foodid)}, {"$push": {"favorites": username}})
            food = mongo.db.foods.find({"_id" : ObjectId(foodid)})
            for element in food:
                number_of_favorites = len(element["favorites"])
                favorites_exist = "favorinot" + str(number_of_favorites)
        return favorites_exist
    else:
        favorites_exist = "no_user"
        return favorites_exist
   
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)