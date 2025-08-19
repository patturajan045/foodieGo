from models import User
from datetime import datetime,timedelta
from .import userBp
from flask import request,jsonify,render_template
from werkzeug.security import generate_password_hash
from mongoengine.queryset.visitor import Q

@userBp.post('/user/new')

def addUser():
    data = request.get_json()
    try:
        if data["name"] =="" or data["email"] =="" or data["password"]=="":
            return jsonify({"status":"error","message":"Missing data required feilds"}),400
        
        if User.objects(email=data["email"]).first():
            return jsonify({
                "status": "error",
                "message": "Email already exists"
            }), 409

        user = User(
            name=data["name"],
            email=data["email"],
            password=generate_password_hash(data["password"]),
            role=data.get("role", "user") 

        )
        user.save()

        return jsonify ({"status":"success","message": "your details addded successfully"}),200
    
    except Exception as e:
        return jsonify({
            "status":"error",
            "message": f"error occured while adding details : {str(e)}"
        }),500 