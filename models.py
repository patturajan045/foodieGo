from mongoengine import Document,StringField,DateTimeField,IntField,BooleanField,EmailField,ReferenceField,CASCADE
from datetime import datetime
from uuid import uuid4
import random

class FoodItems(Document):
    meta = {"collection": "foodItems"}

    id = StringField(primary_key=True, default=lambda: str(uuid4()))
    foodName = StringField(required=True)
    category = StringField()
    price = IntField(default=lambda: random.randint(50, 500))
    restaurantName=StringField()
    specialInstruction=StringField()
    available = BooleanField(default=True)
    addedTime = DateTimeField(default=datetime.now)
    updatedTime = DateTimeField()

class customerDetails(Document):
    meta = {"collection":"customerDetails"}

    id =StringField(primary_key=True,default=lambda:str(uuid4()))
    customerName = StringField(required=True)
    phoneNumber=StringField()
    email =EmailField(unique=True)
    Address = StringField()
    Address2 = StringField()
    city = StringField()
    state = StringField()
    pincode = StringField()
    addedTime = DateTimeField(default=datetime.now)
    updatedTime = DateTimeField()

class myFavorites(Document):
    meta = {"collection":"myFavorites"}
     
    id =StringField(primary_key=True,default=lambda:str(uuid4()))
    foodItems = ReferenceField(FoodItems, required=True , reverse_delete_rule=CASCADE)