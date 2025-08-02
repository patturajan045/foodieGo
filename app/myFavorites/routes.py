from models import myFavorites 
from datetime import datetime,timedelta
from .import myFavoritesBp
from flask import request,jsonify,render_template
from mongoengine.queryset.visitor import Q

@myFavoritesBp.get('/showAll')
def show_all_favorites():
    try:
        favorites = myFavorites.objects()
        data = []

        for fav in favorites:
            food = fav.foodItems 
            data.append({
                "id": str(fav.id),
                "foodName": food.foodName,
                "category": food.category,
                "price": food.price,
                "restaurantName": food.restaurantName,
            })

        return render_template("favorites.html", favorites=data)

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500






