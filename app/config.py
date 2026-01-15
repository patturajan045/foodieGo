import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret_key")
    MONGO_URI = os.environ.get(
        "MONGO_URI",
        "mongodb+srv://foodieGo:Pattu%40123@cluster0.wshic8x.mongodb.net/FoodieGo?retryWrites=true&w=majority"
    )
