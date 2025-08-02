from models import customerDetails
from datetime import datetime,timedelta
from .import customerDetailsBp
from flask import request , jsonify
from mongoengine.queryset.visitor import Q

@customerDetailsBp.post('/new')

def addcustomerDetails():
    data = request.get_json()
    try:
        if data["customerName"] == "" or data["phoneNumber"] == "" or data["email"] == "" or data["Address"] == "" or data["Address2"] == "" or data["city"] == "" or data["city"] == "" or data["state"] == "" or data["pinCode"] == "":
            return jsonify({"status":"error","message":"Missing Required Field"}),400
        
        customerdetails = customerDetails(
            customerName=data["customerName"],
            phoneNumber=data["phoneNumber"],
            email = data["email"],
            Address = data["Address"],
            Address2 = data["Address2"],
            city = data["city"],
            state = data["state"],
            pincode = data["pincode"]
        )
        customerdetails.save()

        
        return jsonify({"status": "success", "message": "Customer Details  added successfully"}), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error occurred while adding new Customer Details: {str(e)}"
        }), 500


