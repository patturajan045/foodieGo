from flask import Blueprint, jsonify, render_template
from pymongo import MongoClient

from . import adminCustomerBp

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["FoodieGo"]
customer_collection = db["customers"]

# -----------------------------
# Page Route
# -----------------------------
@adminCustomerBp.route("/customers")
def admin_customers_page():
    return render_template("admin_customers.html")


# -----------------------------
# API Route: Get Customers
# -----------------------------
@adminCustomerBp.route("/customers/data")
def admin_customers_data():
    customers = []
    for c in customer_collection.find({}, {"password": 0}):
        customers.append({
            "_id": str(c["_id"]),
            "name": c.get("name") or c.get("customerName") or "",
            "email": c.get("email") or "",
            "phone": c.get("phone") or c.get("phoneNumber") or "",
            "city": c.get("city") or (c.get("address") or {}).get("city") or "",
            "state": c.get("state") or (c.get("address") or {}).get("state") or "",
            "pincode": c.get("pincode") or (c.get("address") or {}).get("pincode") or "",
        })
    return jsonify(customers)


# -----------------------------
# API Route: Delete Customer (UUID string IDs)
# -----------------------------
@adminCustomerBp.route("/customers/delete/<id>", methods=["DELETE"])
def delete_customer(id):
    # Delete using string ID directly
    result = customer_collection.delete_one({"_id": id})
    if result.deleted_count == 0:
        return jsonify({"status": "error", "message": "Customer not found"}), 404

    return jsonify({"status": "success", "message": "Customer deleted successfully"})
