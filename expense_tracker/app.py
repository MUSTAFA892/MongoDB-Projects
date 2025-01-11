from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://mustafatinwala6:ZdDhohe700OMzd2u@learningmongo.lof7x.mongodb.net/?retryWrites=true&w=majority&appName=LearningMongo")
db = client["Mongo_db"]
expenses_collection = db["expense"]

@app.route("/")
def home():
    expenses = list(expenses_collection.find())
    total = sum(expense["amount"] for expense in expenses)
    return render_template("index.html", expenses=expenses, total=total)

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        category = request.form["category"]
        amount = float(request.form["amount"])
        date = request.form["date"]
        expenses_collection.insert_one({"category": category, "amount": amount, "date": date})
        return redirect(url_for("home"))
    return render_template("add_expense.html")

@app.route("/delete/<id>")
def delete_expense(id):
    expenses_collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
