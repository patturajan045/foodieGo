from flask import Blueprint, jsonify, render_template, current_app

from .import snacksBp

@snacksBp.route("/", methods=["GET"])
def snacks_page():
    return render_template("snackItems.html")

@snacksBp.route("/all", methods=["GET"])
def get_all_snacks():
    try:
        snack_collection = current_app.mongo_collections["snacks"]
        items = list(snack_collection.find())
        for item in items:
            item["_id"] = str(item["_id"])
            if "imageUrl" not in item:
                item["imageUrl"] = ""
        return jsonify({"status": "success", "data": items}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
