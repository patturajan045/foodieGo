from pymongo import MongoClient
from app.config import Config

# Connect to MongoDB Atlas
client = MongoClient(Config.MONGO_URI)

# IMPORTANT: must match Atlas database name exactly
db = client["foodiego"]

# Collections (case-sensitive)
user_collection     = db["User"]
cart_collection     = db["cart"]
customer_collection = db["customers"]
dessert_collection  = db["desserts"]
food_collection     = db["foods"]
juice_collection    = db["juice"]
order_collection    = db["orders"]
snack_collection    = db["snacks"]

# Test connection
def test_connection():
    try:
        print("Databases:", client.list_database_names())
        print("Collections:", db.list_collection_names())
        print("MongoDB Atlas Connected Successfully")
    except Exception as e:
        print("MongoDB Connection Failed:", e)

if __name__ == "__main__":
    test_connection()
