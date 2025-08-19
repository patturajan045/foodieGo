from flask import jsonify, render_template, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient
from . import adminUserBp

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["FoodieGo"]
user_collection = db["User"]

# Page route (only loads HTML)
@adminUserBp.route("/users")
def admin_users_page():
    return render_template("admin_users.html")

# API route (returns JSON with users)
@adminUserBp.route("/users/data")
def admin_users_data():
    users = list(user_collection.find({}, {"password": 0}))  # exclude password
    for u in users:
        u["_id"] = str(u["_id"])  # convert ObjectId to string
    return jsonify(users)

# Delete route
@adminUserBp.route("/users/delete/<id>", methods=["DELETE"])
def delete_user(id):
    user_collection.delete_one({"_id": ObjectId(id)})
    return jsonify({"status": "success"})
