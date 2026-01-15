from pymongo import MongoClient
from app.config import Config

# Create MongoDB client
client = MongoClient(Config.MONGO_URI)

# Use correct DB name (case-sensitive)
db = client["FoodieGo"]

# Collections
user_collection     = db["User"]
cart_collection     = db["cart"]
customer_collection = db["customers"]
dessert_collection  = db["desserts"]
food_collection     = db["foods"]
juice_collection    = db["juice"]
order_collection    = db["orders"]
snack_collection    = db["snacks"]

def test_connection():
    try:
        print("Databases:", client.list_database_names())
        print("Collections:", db.list_collection_names())
        print("✅ MongoDB Atlas Connected Successfully")
    except Exception as e:
        print("❌ MongoDB Connection Failed:", e)
