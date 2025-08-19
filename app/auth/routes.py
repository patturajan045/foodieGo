from flask import request, jsonify, session , redirect
from werkzeug.security import generate_password_hash ,check_password_hash
from models import User
from . import authBp

@authBp.post('/register')
def register():
    try:
        data = request.get_json()
        print(data)

        # Validate required fields
        required_fields = ["name", "email", "password"]
        if not all(data.get(field) for field in required_fields):
            return jsonify({
                "status": "error",
                "message": "Missing required fields (name, email, password)"
            }), 400

        # Check for duplicate email
        if User.objects(email=data["email"]).first():
            return jsonify({
                "status": "error",
                "message": "Email already registered"
            }), 409
        
        if data["email"].lower() == "patturajan045@gmail.com":
            role = "admin"
        else:
            role = "user"


        # Create and save new user
        user = User(
            name=data["name"],
            email=data["email"],
            password=generate_password_hash(data["password"]),
            role=role
        ).save()

        # Store user info in session
        session["user"] = {
            "id": str(user.id),
            "name": user.name,
            "email": user.email,
            "role": user.role
        }

        return jsonify({
            "status": "success",
            "message": "Register Successfully"
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Server error: {str(e)}"
        }), 500


@authBp.post('/login')
def login():
    data = request.get_json()
    print(data)
    
    try:
        if data["email"] == "" or data["password"] == "":
            return jsonify({"status": "error", "message": "Missing required fields"}), 400

        user = User.objects(email=data["email"]).first()

        if not user:
            return jsonify({"status": "error", "message": "Invalid email or password"}), 401

        if not check_password_hash(user.password, data["password"]):
            return jsonify({"status": "error", "message": "Invalid email or password"}), 401

        session["user"] = {
            "id": str(user.id),
            "name": user.name,
            "email": user.email,
            "role": user.role
        }

        if user.role == "admin":
            redirect_url = "/admin"
        else:
            redirect_url = "/index"

        return jsonify({
            "status": "success",
            "message": "Login successful",
            "redirect": redirect_url
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Server error: {str(e)}"
        }), 500


@authBp.get('/logout')

def logout():
    if session.get('user'):
        session.clear()
        return redirect('/login')
    else:
        return jsonify({"status": "error", "message": "You are not logged in. Please login to continue."})
        
