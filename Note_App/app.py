from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://mustafatinwala6:ZdDhohe700OMzd2u@learningmongo.lof7x.mongodb.net/?retryWrites=true&w=majority&appName=LearningMongo")
db = client["Mongo_db"] 
notes_collection = db["Notes"]

@app.route("/")
def home():
    notes = list(notes_collection.find())
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["GET", "POST"])
def add_note():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        notes_collection.insert_one({"title": title, "content": content})
        return redirect(url_for("home"))
    return render_template("add_note.html")

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_note(id):
    note = notes_collection.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        notes_collection.update_one({"_id": ObjectId(id)}, {"$set": {"title": title, "content": content}})
        return redirect(url_for("home"))
    return render_template("edit_note.html", note=note)

@app.route("/delete/<id>")
def delete_note(id):
    notes_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
