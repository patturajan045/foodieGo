from flask import jsonify, render_template
from . import dessertsBp
from pymongo import MongoClient
from bson import ObjectId

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017')
db = client['FoodieGo']               # Database name
dessert_collection = db['desserts']   # New collection name

# Render HTML page for desserts
@dessertsBp.route('/', methods=['GET'])
def dessert_page():
    return render_template("dessertItems.html")

# Get all dessert items
@dessertsBp.route('/all', methods=['GET'])
def get_all_desserts():
    try:
        items = list(dessert_collection.find())
        for item in items:
            item['_id'] = str(item['_id'])  # Convert ObjectId to string
        return jsonify({
            "status": "success",
            "data": items
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Failed to fetch desserts: {str(e)}"
        }), 500
