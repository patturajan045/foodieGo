from flask import Flask, session
from app.config import Config
from mongoengine import connect, connection
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = ''
    app.config.from_object(Config)

    # Connect MongoEngine
    try:
        connect(host=Config.MONGO_URI)
        if connection.get_connection():
            app.logger.info("MongoEngine Connected Successfully")
    except Exception as error:
        app.logger.error(f"MongoEngine Connection Failed: {error}")

    # Connect PyMongo (for direct collection access in /api/all-items)
    try:
        mongo_client = MongoClient(Config.MONGO_URI)
        app.mongo_db = mongo_client["FoodieGo"]  # store in app for global use
        app.logger.info("PyMongo Connected Successfully")
    except Exception as error:
        app.logger.error(f"PyMongo Connection Failed: {error}")

    # Register Blueprints
    from app.foods import foodsBp
    app.register_blueprint(foodsBp, url_prefix='/foods')

    from app.juice import juiceBp
    app.register_blueprint(juiceBp, url_prefix='/juice')

    from app.desserts import dessertsBp
    app.register_blueprint(dessertsBp, url_prefix='/desserts')

    from app.snacks import snacksBp
    app.register_blueprint(snacksBp, url_prefix='/snacks')

    from app.customer import customerBp
    app.register_blueprint(customerBp,url_prefix='/customer')

    from app.auth import authBp
    app.register_blueprint(authBp, url_prefix='/auth')

    from app.main import main_bp
    app.register_blueprint(main_bp)

    from app.admin import admin_Bp
    app.register_blueprint(admin_Bp)

    from app.user import userBp
    app.register_blueprint(userBp, url_prefix='/user')


    from app.orders import ordersBp
    app.register_blueprint(ordersBp,url_prefix='/orders')

    from app.orderDetails import orderDetailsBp
    app.register_blueprint(orderDetailsBp, url_prefix='/orderDetails')

    from app.cart import cartBp
    app.register_blueprint(cartBp,url_prefix='/cart')

    from app.adminUser import adminUserBp
    app.register_blueprint(adminUserBp,url_prefix='/adminUserBp')

    from app.adminCustomer import adminCustomerBp
    app.register_blueprint(adminCustomerBp)

    from app.adminOrder import adminOrderBp
    app.register_blueprint(adminOrderBp)
    
    # Session Context Processor
    @app.context_processor
    def loadData():
        user = session.get('user')
        if not user:
            return {
                "is_login": False,
                "status": "error",
                "message": "Please login and continue."
            }
        return {
            "is_login": True,
            "name": user.get('name'),
            "email": user.get('email')
        }

    return app
