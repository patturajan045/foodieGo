from flask import Blueprint, request, jsonify, render_template
from models import Cart, User
from datetime import datetime

from . import cartBp

# ✅ Add item to cart
@cartBp.route("/add", methods=["POST"])   # now: /cart/add
def add_to_cart():
    data = request.get_json()
    try:
        user_id = data.get("userId")
        food_id = data.get("foodId")
        food_name = data.get("foodName")
        food_price = data.get("foodPrice")
        image_url = data.get("imageUrl", "")
        quantity = data.get("quantity", 1)

        # Check if item already in cart for same user
        existing_item = Cart.objects(userId=user_id, foodId=food_id).first()
        if existing_item:
            existing_item.quantity += quantity
            existing_item.updatedTime = datetime.now()
            existing_item.save()
            return jsonify({"message": "Cart updated", "cartItem": existing_item.to_dict()}), 200

        # Otherwise create new cart item
        cart_item = Cart(
            userId=user_id,
            foodId=food_id,
            foodName=food_name,
            foodPrice=food_price,
            imageUrl=image_url,
            quantity=quantity,
        )
        cart_item.save()

        return jsonify({"message": "Item added to cart", "cartItem": cart_item.to_dict()}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ✅ Get all items in a user’s cart
@cartBp.route("/<user_id>", methods=["GET"])   # now: /cart/<user_id>
def get_cart(user_id):
    try:
        cart_items = Cart.objects(userId=user_id)
        return jsonify([item.to_dict() for item in cart_items]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ✅ Update quantity of a cart item
@cartBp.route("/update/<item_id>", methods=["PUT"])   # now: /cart/update/<item_id>
def update_cart_item(item_id):
    data = request.get_json()
    try:
        quantity = data.get("quantity")
        cart_item = Cart.objects(id=item_id).first()
        if not cart_item:
            return jsonify({"error": "Cart item not found"}), 404

        cart_item.quantity = quantity
        cart_item.updatedTime = datetime.now()
        cart_item.save()

        return jsonify({"message": "Cart item updated", "cartItem": cart_item.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ✅ Remove item from cart
@cartBp.route("/remove/<item_id>", methods=["DELETE"])   # now: /cart/remove/<item_id>
def remove_cart_item(item_id):
    try:
        cart_item = Cart.objects(id=item_id).first()
        if not cart_item:
            return jsonify({"error": "Cart item not found"}), 404

        cart_item.delete()
        return jsonify({"message": "Cart item removed"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ✅ Clear entire cart for a user
@cartBp.route("/clear/<user_id>", methods=["DELETE"])   # now: /cart/clear/<user_id>
def clear_cart(user_id):
    try:
        Cart.objects(userId=user_id).delete()
        return jsonify({"message": "Cart cleared"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ✅ Test route
@cartBp.route("/", methods=["GET"])    # now: /cart/
def order_page():
    return render_template("card.html")
