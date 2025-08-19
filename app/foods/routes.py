from flask import jsonify, render_template
from . import foodsBp
from pymongo import MongoClient
from bson import ObjectId

# Initialize MongoDB client (adjust connection string as needed)
client = MongoClient('mongodb://localhost:27017')
db = client['FoodieGo']        # your database name
food_collection = db['foods']  # your collection name


@foodsBp.route('/', methods=['GET'])
def customer_details_form():
    return render_template("foodItems.html")

@foodsBp.route('/all', methods=['GET'])
def get_all_food_items():
    try:
        items = list(food_collection.find())
        # Convert ObjectId to string for JSON serialization
        for item in items:
            item['_id'] = str(item['_id'])
        return jsonify({
            "status": "success",
            "data": items
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Failed to fetch items: {str(e)}"
        }), 500
