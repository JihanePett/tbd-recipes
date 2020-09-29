import os
from flask import Flask, render_template, url_for, redirect, request, flash, session, jsonify, make_response, json
from flask_cors import CORS
from pusher import pusher
import simplejson
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import cloudinary as Cloud
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = "myTestDB"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = os.environ.get("SECRET_KEY")
Cloud.config.update = ({
    'cloud_name': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'api_key': os.environ.get('CLOUDINARY_API_KEY'),
    'api_secret': os.environ.get('CLOUDINARY_API_SECRET')
})
pusher.Pusher = ({
    'app_id': os.environ.get('APP_ID'),
    'key': os.environ.get('KEY'),
    'secret': os.environ.get('SECRET'),
    'cluster': os.environ.get('CLUSTER')})

mongo = PyMongo(app)
cors = CORS(app)


@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/new/guest', methods=['POST'])
def guestUser():
    data = request.json
    pusher.trigger(u'general-channel', u'new-guest-details', {
            'name': data['name'],
            'email': data['email']
        })
    return json.dumps(data)


@app.route("/pusher/auth", methods=['POST'])
def pusher_authentication():
    auth = pusher.authenticate(channel=request.form['channel_name'],
                               socket_id=request.form['socket_id'])
    return json.dumps(auth)


@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html',
                           recipes=mongo.db.recipes.find())


@app.route('/my_recipes')
def my_recipes():
    return render_template('myrecipes.html',
                           recipes=mongo.db.recipes.find())


@app.route('/search_recipes', methods=["GET", "POST"])
def search_recipes():
    query = request.form.get("query")
    recipes = mongo.db.recipes.find({"$text": {"$search": query}})
    return render_template('myrecipes.html', recipes=recipes)


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           categories=mongo.db.categories.find(),
                           types=mongo.db.types.find(),
                           people=mongo.db.people.find(),
                           preptimes=mongo.db.preptimes.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    all_types = mongo.db.types.find()
    all_people = mongo.db.people.find()
    all_preptimes = mongo.db.preptimes.find()
    return render_template('editrecipe.html',
                           recipe=the_recipe, categories=all_categories,
                           types=all_types, people=all_people,
                           preptimes=all_preptimes)


@app.route('/update_recipe/<recipe_id>', methods=["POST", "GET"])
def update_recipe(recipe_id):
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
                            {'recipe_name': request.form.get('recipe_name'),
                             'category_name':
                             request.form.get('category_name'),
                             'type_select':
                             request.form.get('type_select'),
                             'recipe_description':
                             request.form.get('recipe_description'),
                             'recipe_ingredients':
                             request.form.get('recipe_ingredients'),
                             'recipe_method':
                             request.form.get('recipe_method'),
                             'preparation_time':
                             request.form.get('preparation_time'),
                             'number_people':
                             request.form.get('number_people'),
                             'image_url': request.form.get('image_url'),
                             'pdf': request.form.get('pdf')})
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                            "get_recipes", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("my_recipes"))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=mongo.db.categories.find_one(
                                    {'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['GET', 'POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


@app.route('/insert_category', methods=['GET', 'POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
            request.form["name"]
        ))
    return render_template("contact.html", page_title="Contact")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/thermomix')
def thermomix():
    return render_template('thermomix.html')


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=(int(os.environ.get('PORT'))),
            debug=True)
