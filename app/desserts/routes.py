from flask import Blueprint, jsonify, render_template, current_app

from .import dessertsBp

@dessertsBp.route("/", methods=["GET"])
def desserts_page():
    return render_template("dessertItems.html")

@dessertsBp.route("/all", methods=["GET"])
def get_all_desserts():
    try:
        dessert_collection = current_app.mongo_collections["desserts"]
        items = list(dessert_collection.find())
        for item in items:
            item["_id"] = str(item["_id"])
            if "imageUrl" not in item:
                item["imageUrl"] = ""
        return jsonify({"status": "success", "data": items}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
