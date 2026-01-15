from flask import Blueprint, jsonify, session, render_template, current_app
from bson import ObjectId

from .import orderDetailsBp

# -----------------
# GET MY ORDERS
# -----------------
@orderDetailsBp.route("/myOrders", methods=["GET"])
def get_my_orders():
    if "user" not in session:
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    orders_collection = current_app.mongo_collections["orders"]
    user_id = session["user"]["id"]

    orders = list(orders_collection.find({"userId": user_id}))

    if not orders:
        return jsonify({
            "status": "success",
            "data": [],
            "message": "No orders found"
        }), 200

    data = []
    for order in orders:
        data.append({
            "orderId": str(order["_id"]),
            "restaurant": order.get("restaurant"),
            "foodName": order.get("foodName"),
            "quantity": order.get("quantity"),
            "paymentMethod": order.get("paymentMethod"),
            "date": order.get("orderDate").strftime("%Y-%m-%d %H:%M")
                    if order.get("orderDate") else ""
        })

    return jsonify({"status": "success", "data": data}), 200


# -----------------
# DELETE ORDER
# -----------------
@orderDetailsBp.route("/delete/<order_id>", methods=["DELETE"])
def delete_order(order_id):
    if "user" not in session:
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    orders_collection = current_app.mongo_collections["orders"]
    user_id = session["user"]["id"]

    result = orders_collection.delete_one({
        "_id": ObjectId(order_id),
        "userId": user_id
    })

    if result.deleted_count == 0:
        return jsonify({
            "status": "error",
            "message": "Order not found"
        }), 404

    return jsonify({
        "status": "success",
        "message": "Order deleted successfully"
    }), 200


# -----------------
# PAGE ROUTE
# -----------------
@orderDetailsBp.route("/", methods=["GET"])
def order_page():
    return render_template("orderDetails.html")
