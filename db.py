from pymongo import MongoClient
from app.config import Config

client = MongoClient(Config.MONGO_URI)
db = client["foodieGo"]

user_collection = db["User"]
cart_collection = db["cart"]
customer_collection = db["customers"]
dessert_collection = db["desserts"]
food_collection = db["foods"]
juice_collection = db["juice"]
order_collection = db["orders"]
snack_collection = db["snacks"]

# Optional test function
def test_connection():
    try:
        print("Databases:", client.list_database_names())
        print("Collections in FoodieGo:", db.list_collection_names())
        print("✅ MongoDB connection successful!")
    except Exception as e:
        print("❌ MongoDB connection failed:", e)

if __name__ == "__main__":
    test_connection()
