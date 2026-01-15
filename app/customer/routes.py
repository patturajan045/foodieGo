from flask import Blueprint, request, jsonify, current_app, render_template, session
from uuid import uuid4
from datetime import datetime

from .import customerBp

# ---------------------------
# ADD CUSTOMER
# ---------------------------
@customerBp.route("/", methods=["POST"])
def add_customer():
    user = session.get("user")
    if not user:
        return jsonify({"status": "error", "message": "User not logged in"}), 401

    data = request.get_json(force=True) or {}

    required = ["customerName", "phone", "email", "address", "city", "state", "pincode"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return jsonify({"status": "error", "message": f"Missing fields: {', '.join(missing)}"}), 400

    customer_collection = current_app.mongo_collections["customers"]

    customer_data = {
        "_id": str(uuid4()),
        "userEmail": user["email"],
        "customerName": data["customerName"].strip(),
        "phone": data["phone"].strip(),
        "email": data["email"].strip().lower(),
        "address": data["address"].strip(),
        "address2": data.get("address2", "").strip(),
        "city": data["city"].strip(),
        "state": data["state"].strip(),
        "pincode": str(data["pincode"]).strip(),
        "createdAt": datetime.utcnow()
    }

    customer_collection.insert_one(customer_data)

    return jsonify({"status": "success", "message": "Customer added successfully"}), 201


# ---------------------------
# GET ALL CUSTOMERS
# ---------------------------
@customerBp.route("/all", methods=["GET"])
def get_all_customers():
    user = session.get("user")
    if not user:
        return jsonify({"status": "error", "message": "Not logged in"}), 401

    customer_collection = current_app.mongo_collections["customers"]

    customers = list(customer_collection.find({"userEmail": user["email"]}))
    for c in customers:
        c["_id"] = str(c["_id"])

    return jsonify({"status": "success", "data": customers})


# ---------------------------
# DELETE CUSTOMER
# ---------------------------
@customerBp.route("/<customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    user = session.get("user")
    if not user:
        return jsonify({"status": "error", "message": "Not logged in"}), 401

    customer_collection = current_app.mongo_collections["customers"]

    result = customer_collection.delete_one({
        "_id": customer_id,
        "userEmail": user["email"]
    })

    if result.deleted_count == 0:
        return jsonify({"status": "error", "message": "Customer not found"}), 404

    return jsonify({"status": "success", "message": "Customer deleted successfully"})


# ---------------------------
# RENDER HTML FORM
# ---------------------------
@customerBp.route("/", methods=["GET"])
def customer_details_form():
    return render_template("customer.html")
