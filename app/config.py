import os

class Config:
    # Flask secret key
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret_key")

    # MongoDB connection string
    MONGO_URI = os.environ.get(
        "MONGO_URI",
        "mongodb+srv://patturajan045:MrsfSc1lQ8HKRuWU@cluster0.wshic8x.mongodb.net/FoodieGo?retryWrites=true&w=majority"
    )
