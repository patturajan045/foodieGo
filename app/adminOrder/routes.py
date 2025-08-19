from flask import Blueprint, jsonify, render_template
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId

from .import adminOrderBp

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["FoodieGo"]
order_collection = db["orders"]  # make sure collection name matches

# Page route → loads HTML template
@adminOrderBp.route("/orders")
def admin_orders_page():
    return render_template("admin_orders.html")

# API route → returns all orders
@adminOrderBp.route("/orders/data")
def admin_orders_data():
    orders = []
    for o in order_collection.find({}):
        orders.append({
            "_id": str(o["_id"]),
            "restaurant": o.get("restaurant"),
            "foodName": o.get("foodName"),
            "quantity": o.get("quantity"),
            "couponCode": o.get("couponCode"),
            "specialInstructions": o.get("specialInstructions"),
            "paymentMethod": o.get("paymentMethod"),
            "deliveryTimePreference": o.get("deliveryTimePreference"),
            "tipAmount": o.get("tipAmount"),
            "orderDate": str(o.get("orderDate")),
        })
    return jsonify(orders)

# Delete route → delete by ID
@adminOrderBp.route("/orders/delete/<id>", methods=["DELETE"])
def delete_order(id):
    result = order_collection.delete_one({"_id": id})
    if result.deleted_count == 0:
        return jsonify({"status": "error", "message": "Order not found"}), 404
    return jsonify({"status": "success"})
