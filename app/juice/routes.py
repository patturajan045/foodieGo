from flask import Blueprint, jsonify, render_template, current_app

from .import juiceBp

@juiceBp.route("/", methods=["GET"])
def juice_page():
    return render_template("juiceItems.html")

@juiceBp.route("/all", methods=["GET"])
def get_all_juice_items():
    try:
        juice_collection = current_app.mongo_collections["juice"]
        items = list(juice_collection.find())
        for item in items:
            item["_id"] = str(item["_id"])
            if "imageUrl" not in item:
                item["imageUrl"] = ""
        return jsonify({"status": "success", "data": items}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
