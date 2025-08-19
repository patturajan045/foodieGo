from flask import Blueprint, request, jsonify ,session
from datetime import datetime
from models import Order
from uuid import uuid4

from .import ordersBp


@ordersBp.route('/', methods=['POST'])
def create_order():
    if "user" not in session:
        return jsonify({"status": "error", "message": "Unauthorized"}), 401

    user = session["user"]   # 👈 current logged-in user
    user_id = user["id"]

    data = request.get_json(force=True)
    try:
        restaurant = data.get('restaurant')
        paymentMethod = data.get('paymentMethod')
        items = data.get('items')

        if not restaurant or not paymentMethod or not items:
            return jsonify({"status": "error", "message": "Missing required fields"}), 400

        saved_order_ids = []
        orderDate = datetime.now()

        for item in items:
            order = Order(
                id=str(uuid4()),
                userId=user_id,   # 👈 link order to current user
                restaurant=restaurant,
                foodName=item.get('foodName'),
                quantity=int(item.get('quantity', 1)),
                couponCode=data.get('couponCode'),
                specialInstructions=data.get('specialInstructions'),
                paymentMethod=paymentMethod,
                deliveryTimePreference=data.get('deliveryTimePreference', 'ASAP'),
                scheduledDelivery=None,
                tipAmount=float(data.get('tipAmount', 0.0)),
                orderDate=orderDate,
                addedTime=orderDate,
                updatedTime=None
            )
            order.save()
            saved_order_ids.append(str(order.id))

        return jsonify({
            "status": "success",
            "message": "Order placed",
            "orderIds": saved_order_ids
        }), 201


    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@ordersBp.route('/<order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = Order.objects.get(id=order_id)
        order_data = {
            "id": str(order.id),
            "restaurant": order.restaurant,
            "foodName": order.foodName,
            "quantity": order.quantity,
            "couponCode": order.couponCode,
            "specialInstructions": order.specialInstructions,
            "paymentMethod": order.paymentMethod,
            "deliveryTimePreference": order.deliveryTimePreference,
            "scheduledDelivery": order.scheduledDelivery.isoformat() if order.scheduledDelivery else None,
            "tipAmount": order.tipAmount,
            "orderDate": order.orderDate.isoformat() if order.orderDate else None,
            "addedTime": order.addedTime.isoformat() if order.addedTime else None,
            "updatedTime": order.updatedTime.isoformat() if order.updatedTime else None,
        }
        return jsonify(order_data), 200

    except Order.DoesNotExist:
        return jsonify({"error": "Order not found"}), 404
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500
