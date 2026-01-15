from pymongo import MongoClient
from app.config import Config

client = MongoClient(Config.MONGO_URI)
db = client["FoodieGo"]

user_collection = db["User"]
cart_collection = db["Cart"]
customer_collection = db["Customers"]
dessert_collection = db["Desserts"]
food_collection = db["Foods"]
juice_collection = db["Juice"]
order_collection = db["Orders"]
snack_collection = db["Snacks"]

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
