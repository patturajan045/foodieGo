from mongoengine import Document, StringField, EmailField, DateTimeField, FloatField, IntField, BooleanField, ListField, ReferenceField,CASCADE
from datetime import datetime
from uuid import uuid4
from mongoengine import ListField



# Existing Customer Details
class customerDetails(Document):
    meta = {"collection":"customerDetails"}

    id =StringField(primary_key=True,default=lambda:str(uuid4()))
    customerName = StringField(required=True)
    phoneNumber=StringField()
    email =EmailField(required=True)
    Address = StringField()
    Address2 = StringField()
    city = StringField()
    state = StringField()
    pincode = StringField()
    addedTime = DateTimeField(default=datetime.now)
    updatedTime = DateTimeField()

# Existing User Model
class User(Document):
    meta = {"collection": "User"}
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    role = StringField(default='user')


class Order(Document):
    meta = {"collection": "orders"}

    id = StringField(primary_key=True, default=lambda: str(uuid4()))
    userId = StringField(required=True) 
    restaurant = StringField(required=True)
    foodName = StringField(required=True)
    quantity = IntField(default=1)
    couponCode = StringField()
    specialInstructions = StringField()
    paymentMethod = StringField()
    deliveryTimePreference = StringField(default="ASAP")
    scheduledDelivery = DateTimeField()
    tipAmount = FloatField(default=0.0)
    orderDate = DateTimeField(default=datetime.now)
    addedTime = DateTimeField(default=datetime.now)
    updatedTime = DateTimeField()

class Cart(Document):
    meta = {"collection": "cart"}

    id = StringField(primary_key=True, default=lambda: str(uuid4()))
    userId = ReferenceField("User", reverse_delete_rule=CASCADE, required=True)
    foodId = StringField(required=True)
    foodName = StringField(required=True)
    foodPrice = FloatField(required=True)
    quantity = IntField(default=1, min_value=1)
    imageUrl = StringField()
    addedTime = DateTimeField(default=datetime.now)
    updatedTime = DateTimeField(default=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "userId": str(self.userId.id) if self.userId else None,
            "foodId": self.foodId,
            "foodName": self.foodName,
            "foodPrice": self.foodPrice,
            "quantity": self.quantity,
            "imageUrl": self.imageUrl,
            "addedTime": self.addedTime.isoformat() if self.addedTime else None,
            "updatedTime": self.updatedTime.isoformat() if self.updatedTime else None,
        }









