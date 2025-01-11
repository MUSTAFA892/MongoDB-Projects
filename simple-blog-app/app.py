from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Flask app setup
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

# Database
db = mongo.db
posts_collection = db["posts"]
users_collection = db["users"]

# Routes
@app.route('/')
def index():
    posts = posts_collection.find()
    return render_template('index.html', posts=posts)

@app.route('/post/<post_id>')
def post(post_id):
    post = posts_collection.find_one({"_id": ObjectId(post_id)})
    return render_template('post.html', post=post)

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        posts_collection.insert_one({'title': title, 'content': content, 'author': session['username']})
        flash('Post added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_post.html')

@app.route('/edit_post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = posts_collection.find_one({"_id": ObjectId(post_id)})
    if 'username' not in session or post['author'] != session['username']:
        return redirect(url_for('login'))

    if request.method == 'POST':
        posts_collection.update_one(
            {'_id': ObjectId(post_id)},
            {'$set': {'title': request.form.get('title'), 'content': request.form.get('content')}}
        )
        flash('Post updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_post.html', post=post)

@app.route('/delete_post/<post_id>')
def delete_post(post_id):
    post = posts_collection.find_one({"_id": ObjectId(post_id)})
    if 'username' not in session or post['author'] != session['username']:
        return redirect(url_for('login'))
    
    posts_collection.delete_one({"_id": ObjectId(post_id)})
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_hash = generate_password_hash(password)

        if users_collection.find_one({"username": username}):
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        
        users_collection.insert_one({'username': username, 'password': password_hash})
        flash('User registered successfully!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = users_collection.find_one({"username": username})
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password!', 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
