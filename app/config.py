import os 

class Config:
    SECRET_KEY = 'your_very_secret_key_here'
    MONGO_URI = os.getenv('MONGO_URI','mongodb://localhost:27017/FoodieGo')