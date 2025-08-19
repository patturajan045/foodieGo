from flask import jsonify, render_template
from . import snacksBp
from pymongo import MongoClient
from bson import ObjectId

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017')
db = client['FoodieGo']             # Database name
snack_collection = db['snacks']     # Snacks collection

# Render HTML page for snacks
@snacksBp.route('/', methods=['GET'])
def snack_page():
    return render_template("snackItems.html")

# Get all snack items
@snacksBp.route('/all', methods=['GET'])
def get_all_snacks():
    try:
        items = list(snack_collection.find())
        for item in items:
            item['_id'] = str(item['_id'])  # Convert ObjectId to string
        return jsonify(status="success", data=items), 200
    except Exception as e:
        return jsonify(status="error", message=f"Failed to fetch snacks: {str(e)}"), 500
