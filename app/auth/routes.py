from flask import request, jsonify, session, redirect, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from . import authBp


# ---------------- REGISTER ----------------
@authBp.post('/register')
def register():
    try:
        data = request.get_json()

        # Validate fields
        if not data or not data.get("name") or not data.get("email") or not data.get("password"):
            return jsonify({
                "status": "error",
                "message": "Missing required fields (name, email, password)"
            }), 400

        users = current_app.mongo_collections["user"]

        # Check duplicate email
        if users.find_one({"email": data["email"]}):
            return jsonify({
                "status": "error",
                "message": "Email already registered"
            }), 409

        # Role
        role = "admin" if data["email"].lower() == "patturajan045@gmail.com" else "user"

        # Create user
        user = {
            "name": data["name"],
            "email": data["email"],
            "password": generate_password_hash(data["password"]),
            "role": role
        }

        result = users.insert_one(user)

        # Store session
        session["user"] = {
            "id": str(result.inserted_id),
            "name": user["name"],
            "email": user["email"],
            "role": role
        }

        return jsonify({
            "status": "success",
            "message": "Registered Successfully"
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Server error: {str(e)}"
        }), 500


# ---------------- LOGIN ----------------
@authBp.post('/login')
def login():
    try:
        data = request.get_json()

        if not data or not data.get("email") or not data.get("password"):
            return jsonify({"status": "error", "message": "Missing required fields"}), 400

        users = current_app.mongo_collections["user"]

        user = users.find_one({"email": data["email"]})

        if not user:
            return jsonify({"status": "error", "message": "Invalid email or password"}), 401

        if not check_password_hash(user["password"], data["password"]):
            return jsonify({"status": "error", "message": "Invalid email or password"}), 401

        session["user"] = {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "role": user["role"]
        }

        redirect_url = "/admin" if user["role"] == "admin" else "/index"

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


# ---------------- LOGOUT ----------------
@authBp.get('/logout')
def logout():
    session.clear()
    return redirect('/login')
