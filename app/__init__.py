from flask import Flask
from app.config import Config
from mongoengine import connect,connection

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    try:
        connect(host = Config.MONGO_URI)
        if connection.get_connection():
            app.logger.info("database Connected Successfully")

    except Exception as error:
        app.logger.error(f"Connection Failed :{error}")

    from app.foodItems import foodItemsBp
    app.register_blueprint(foodItemsBp,url_prefix = '/foodItems')

    from app.customerDetails import customerDetailsBp
    app.register_blueprint(customerDetailsBp, url_prefix='/customerDetails')
    
    from app.myFavorites import myFavoritesBp
    app.register_blueprint(myFavoritesBp,url_prefix='/myFavorites')
    return app