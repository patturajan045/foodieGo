from pymongo import MongoClient

# MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://patturajan045:MrsfSc1lQ8HKRuWU@cluster0.wshic8x.mongodb.net/FoodieGo?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)

# Select DB
db = client["FoodieGo"]

# Collections
user_collection = db["User"]
cart_collection = db["Cart"]
customer_collection = db["Customers"]
dessert_collection = db["Desserts"]
food_collection = db["Foods"]
juice_collection = db["Juice"]
order_collection = db["Orders"]
snack_collection = db["Snacks"]

# --- Test connection ---
if __name__ == "__main__":
    try:
        print("Databases:", client.list_database_names())
        print("Collections in FoodieGo:", db.list_collection_names())
        print("✅ MongoDB connection successful!")
    except Exception as e:
        print("❌ MongoDB connection failed:", e)
