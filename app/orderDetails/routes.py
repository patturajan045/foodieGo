from flask import Blueprint, jsonify, session, render_template
from models import Order  # your MongoEngine Order model

from . import orderDetailsBp


# ----------------- API ROUTES -----------------
@orderDetailsBp.route('/myOrders', methods=['GET'])
def get_my_orders():
    if "user" not in session:
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    user_id = session["user"]["id"]
    orders = Order.objects(userId=user_id)

    if not orders:
        return jsonify({"status": "success", "data": [], "message": "No orders found"}), 200

    data = [
        {
            "orderId": str(order.id),
            "restaurant": order.restaurant,
            "foodName": order.foodName,
            "quantity": order.quantity,
            "paymentMethod": order.paymentMethod,
            "date": order.orderDate.strftime("%Y-%m-%d %H:%M"),
        }
        for order in orders 
    ]

    return jsonify({"status": "success", "data": data}), 200


@orderDetailsBp.route('/delete/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    if "user" not in session:
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    user_id = session["user"]["id"]
    order = Order.objects(id=order_id, userId=user_id).first()

    if not order:
        return jsonify({"status": "error", "message": "Order not found"}), 404

    order.delete()
    return jsonify({"status": "success", "message": "Order deleted successfully"}), 200


# ----------------- PAGE ROUTE -----------------
@orderDetailsBp.route('/', methods=['GET'])
def order_page():
    return render_template("orderDetails.html")
