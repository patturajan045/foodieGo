from flask import Blueprint, jsonify, render_template, current_app
from .import foodsBp

@foodsBp.route("/", methods=["GET"])
def food_page():
    return render_template("foodItems.html")

@foodsBp.route("/all", methods=["GET"])
def get_all_food_items():
    try:
        food_collection = current_app.mongo_collections["foods"]
        items = list(food_collection.find())
        for item in items:
            item["_id"] = str(item["_id"])
            if "imageUrl" not in item:
                item["imageUrl"] = ""  # placeholder if no image
        return jsonify({"status": "success", "data": items}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
