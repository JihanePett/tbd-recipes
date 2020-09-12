import os
from flask import Flask, render_template, url_for, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = "myTestDB"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html',
                           recipes=mongo.db.recipes.find().limit(2))


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html',
                           recipe=the_recipe, categories=all_categories)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
                   {'recipe_name': request.form.get('recipe_name'),
                    'category_name': request.form.get('category_name'),
                    'recipe_description':
                    request.form.get('recipe_description'),
                    'recipe_ingredients':
                    request.form.get('recipe_ingredients'),
                    'recipe_method': request.form.get('recipe_method'),
                    'preparation_time': request.form.get('preparation_time'),
                    'number_people': request.form.get('number_people'),
                    'is_difficult': request.form.get('is_difficult')})
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
            return redirect(url_for('editrecipe'))
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=(int(os.environ.get('PORT'))),
            debug=True)
