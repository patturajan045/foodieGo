from flask import Blueprint, request, jsonify, session, current_app
from datetime import datetime
from uuid import uuid4

ordersBp = Blueprint("orders", __name__)

# ---------------------------
# CREATE ORDER
# ---------------------------
@ordersBp.route("/", methods=["POST"])
def create_order():
    if "user" not in session:
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    user = session["user"]
    user_id = user["id"]

    data = request.get_json(force=True) or {}

    restaurant = data.get("restaurant")
    paymentMethod = data.get("paymentMethod")
    items = data.get("items")

    if not restaurant or not paymentMethod or not items:
        return jsonify({
            "status": "error",
            "message": "Missing required fields"
        }), 400

    orders_collection = current_app.mongo_collections["orders"]

    saved_order_ids = []
    now = datetime.utcnow()

    try:
        for item in items:
            order_data = {
                "_id": str(uuid4()),
                "userId": user_id,
                "restaurant": restaurant,
                "foodName": item.get("foodName"),
                "quantity": int(item.get("quantity", 1)),
                "couponCode": data.get("couponCode"),
                "specialInstructions": data.get("specialInstructions"),
                "paymentMethod": paymentMethod,
                "deliveryTimePreference": data.get("deliveryTimePreference", "ASAP"),
                "scheduledDelivery": None,
                "tipAmount": float(data.get("tipAmount", 0.0)),
                "orderDate": now,
                "addedTime": now,
                "updatedTime": None
            }

            orders_collection.insert_one(order_data)
            saved_order_ids.append(order_data["_id"])

        return jsonify({
            "status": "success",
            "message": "Order placed successfully",
            "orderIds": saved_order_ids
        }), 201

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Server error: {str(e)}"
        }), 500


# ---------------------------
# GET SINGLE ORDER
# ---------------------------
@ordersBp.route("/<order_id>", methods=["GET"])
def get_order(order_id):
    orders_collection = current_app.mongo_collections["orders"]

    try:
        order = orders_collection.find_one({"_id": order_id})

        if not order:
            return jsonify({"status": "error", "message": "Order not found"}), 404

        order_data = {
            "id": order["_id"],
            "restaurant": order.get("restaurant"),
            "foodName": order.get("foodName"),
            "quantity": order.get("quantity"),
            "couponCode": order.get("couponCode"),
            "specialInstructions": order.get("specialInstructions"),
            "paymentMethod": order.get("paymentMethod"),
            "deliveryTimePreference": order.get("deliveryTimePreference"),
            "scheduledDelivery": order.get("scheduledDelivery"),
            "tipAmount": order.get("tipAmount"),
            "orderDate": order.get("orderDate").isoformat() if order.get("orderDate") else None,
            "addedTime": order.get("addedTime").isoformat() if order.get("addedTime") else None,
            "updatedTime": order.get("updatedTime")
        }

        return jsonify({"status": "success", "data": order_data}), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Server error: {str(e)}"
        }), 500
