from models import FoodItems
from datetime import datetime,timedelta
from .import foodItemsBp
from flask import request ,jsonify
from mongoengine.queryset.visitor import Q

@foodItemsBp.post('/new')
def addfoodItems():
    data = request.get_json()

    try:
        # Check for required fields
        required_fields = ["foodName", "category", "restaurantName"]
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    "status": "error",
                    "message": f"Missing required field: {field}"
                }), 400

        # Validate and set price
        price = data.get("price")
        if price is not None and price != "":
            try:
                price = int(price)
            except ValueError:
                return jsonify({
                    "status": "error",
                    "message": "Price must be an integer"
                }), 400
        else:
            # Auto-generate price if not provided
            import random
            price = random.randint(50, 500)

        # Create food item
        food_item = FoodItems(
            foodName=data["foodName"],
            category=data["category"],
            price=price,
            restaurantName=data["restaurantName"],
            available=data.get("available", True),
            specialInstruction=data.get("specialInstruction", "")
        )
        food_item.save()

        return jsonify({
            "status": "success",
            "message": "Food item added successfully",
            "data": {
                "id": str(food_item.id),
                "foodName": food_item.foodName,
                "price": food_item.price
            }
        }), 201

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error occurred while adding new food item: {str(e)}"
        }), 500








