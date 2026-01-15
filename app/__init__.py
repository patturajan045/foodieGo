from flask import Flask, session, current_app
from app.config import Config
from db import (
    user_collection,
    cart_collection,
    customer_collection,
    dessert_collection,
    food_collection,
    juice_collection,
    order_collection,
    snack_collection
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Store collections in app context
    app.mongo_collections = {
        "user": user_collection,
        "cart": cart_collection,
        "customer": customer_collection,
        "dessert": dessert_collection,
        "food": food_collection,
        "juice": juice_collection,
        "order": order_collection,
        "snack": snack_collection
    }

    # --- Register Blueprints ---
    from app.foods import foodsBp
    app.register_blueprint(foodsBp, url_prefix='/foods')

    from app.juice import juiceBp
    app.register_blueprint(juiceBp, url_prefix='/juice')

    from app.desserts import dessertsBp
    app.register_blueprint(dessertsBp, url_prefix='/desserts')

    from app.snacks import snacksBp
    app.register_blueprint(snacksBp, url_prefix='/snacks')

    from app.customer import customerBp
    app.register_blueprint(customerBp, url_prefix='/customer')

    from app.auth import authBp
    app.register_blueprint(authBp, url_prefix='/auth')

    from app.main import main_bp
    app.register_blueprint(main_bp)

    from app.admin import admin_Bp
    app.register_blueprint(admin_Bp)

    from app.user import userBp
    app.register_blueprint(userBp, url_prefix='/user')

    from app.orders import ordersBp
    app.register_blueprint(ordersBp, url_prefix='/orders')

    from app.orderDetails import orderDetailsBp
    app.register_blueprint(orderDetailsBp, url_prefix='/orderDetails')

    from app.cart import cartBp
    app.register_blueprint(cartBp, url_prefix='/cart')

    from app.adminUser import adminUserBp
    app.register_blueprint(adminUserBp, url_prefix='/adminUserBp')

    from app.adminCustomer import adminCustomerBp
    app.register_blueprint(adminCustomerBp)

    from app.adminOrder import adminOrderBp
    app.register_blueprint(adminOrderBp)

    # --- Session Context Processor ---
    @app.context_processor
    def loadData():
        user = session.get('user')
        if not user:
            return {"is_login": False, "status": "error", "message": "Please login and continue."}
        return {"is_login": True, "name": user.get('name'), "email": user.get('email')}

    # --- Optional test route ---
    @app.route('/test-db')
    def test_db():
        try:
            foods = list(current_app.mongo_collections["food"].find({}))
            return {"status": "success", "foods_count": len(foods)}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    return app
