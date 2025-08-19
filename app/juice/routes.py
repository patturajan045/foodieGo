from flask import jsonify, render_template
from . import juiceBp
from pymongo import MongoClient
from bson import ObjectId

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017')
db = client['FoodieGo']              # Database
food_collection = db['juice']        # Single collection for all foods

# Render HTML page
@juiceBp.route('/', methods=['GET'])
def customer_details_form():
    return render_template("juiceItems.html")

# Get all food items

@juiceBp.route('/all', methods=['GET'])
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


