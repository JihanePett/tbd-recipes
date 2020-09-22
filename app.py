import os
import re
from flask import Flask, render_template, url_for, redirect, request, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import cloudinary as Cloud
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = "myTestDB"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
Cloud.config.update = ({
    'cloud_name': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'api_key': os.environ.get('CLOUDINARY_API_KEY'),
    'api_secret': os.environ.get('CLOUDINARY_API_SECRET')
})

mongo = PyMongo(app)


@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html',
                           recipes=mongo.db.recipes.find())


@app.route('/my_recipes')
def my_recipes():
    return render_template('myrecipes.html',
                           recipes=mongo.db.recipes.find())


@app.route('/search_recipes')
def search_recipes():
    if (request.args.get('recipe_name') is not None
            or request.args.get('category_name') is not None):
        recipename = None
        categoryname = None

        if request.args.get('recipe_name') is not None and request.args.get('recipe_name') != '':
            recipenameregex = "\\W*" + request.args.get("recipe_name") + "\\W*"
            recipename = re.compile(recipenameregex, re.IGNORECASE)
        if request.args.get('category_name') is not None and request.args.get('category_name') != '':
            categoryregex = "\\W*" + request.args.get("category_name") + "\\W*"
            categoryname = re.compile(categoryregex, re.IGNORECASE)
        recipes = mongo.db.recipes.find({"$or": [{"recipe_name": recipename},
                                                 {"category_name": categoryname}]})
        return render_template("myrecipes.html",
                               recipes=recipes,
                               categories=mongo.db.categories.find())
    return render_template("myrecipes.html",
                           recipes=mongo.db.recipes.find(),
                           categories=mongo.db.categories.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           categories=mongo.db.categories.find(),
                           types=mongo.db.types.find())


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
    return render_template('editrecipe.html',
                           recipe=the_recipe, categories=all_categories,
                           types=all_types)


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
                             'image_url': request.form.get('image_url')})
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Please try again'
        else:
            return redirect(url_for('get_recipes'))
    return render_template('login.html', error=error)


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


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=(int(os.environ.get('PORT'))),
            debug=True)
