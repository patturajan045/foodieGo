# 🎯 FoodieGo – Full-Stack Food Ordering Application

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?logo=flask&logoColor=black)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-5.0-green?logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Postman](https://img.shields.io/badge/Postman-202020?logo=postman&logoColor=orange)](https://www.postman.com/)

---

## 🚀 Project Overview

**FoodieGo** is a full-stack **food ordering web application** built using **Flask** and **MongoDB**.  
It allows users to **browse food items, manage a cart, and place orders** with delivery preferences. The app includes **user authentication, order management, and backend API handling** for seamless functionality.

---

## 🛠️ Features

- 🔑 **User Authentication** – Secure registration and login system.  
- 🛒 **Cart Management** – Add, update, and remove food items from the cart.  
- 🍽️ **Order Processing** – Place orders with quantity, tip, and delivery preferences.  
- 🗂️ **Customer Management** – Store and manage customer addresses and contact details.  
- 🔒 **Backend APIs** – RESTful APIs implemented using Flask and MongoEngine.  
- 📱 **Responsive Frontend** – Built with HTML, CSS, JavaScript, and Bootstrap.  
- 🧪 **API Testing** – Endpoints tested and validated using Postman.  

---

## 🗃️ Data Models

FoodieGo uses **MongoDB** with **MongoEngine** ODM. Key models:

### 1️⃣ User
- `id`, `name`, `email`, `password`, `role`  
- Timestamps: `addedTime`, `updatedTime`  

### 2️⃣ CustomerDetails
- `id`, `customerName`, `phoneNumber`, `email`, `Address`, `city`, `state`, `pincode`  
- Timestamps: `addedTime`, `updatedTime`  

### 3️⃣ Cart
- `id`, `userId`, `foodId`, `foodName`, `foodPrice`, `quantity`, `imageUrl`  
- Timestamps: `addedTime`, `updatedTime`  

### 4️⃣ Order
- `id`, `userId`, `restaurant`, `foodName`, `quantity`, `couponCode`, `specialInstructions`  
- `paymentMethod`, `deliveryTimePreference`, `scheduledDelivery`, `tipAmount`  
- Timestamps: `orderDate`, `addedTime`, `updatedTime`  

> This structure ensures **scalable data management** and **efficient backend operations**.

---

## 🖥️ Technology Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask, MongoEngine |
| Frontend | HTML5, CSS3, JavaScript, Bootstrap |
| Database | MongoDB |
| API Testing | Postman |
| Version Control | Git & GitHub |

---

## ⚡ Installation & Setup

1. **Clone the repo**

```bash
git clone https://github.com/<yourusername>/FoodieGo.git
cd FoodieGo


1. Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate 


Install dependencies: 

pip install -r requirements.txt
 

Set up MongoDB
Make sure MongoDB is running locally or use a cloud MongoDB URI. Update the connection string in app.py.

Run the application: 
python app.py 

Open in browser:
Navigate to http://127.0.0.1:5000/ to view the application. 

Usage

Browse food items and add them to the cart

Manage cart items and place orders 

Learning Outcomes

Built a full-stack web application with Python Flask and MongoDB

Gained experience in RESTful API development, database modeling, and backend validation

Practiced frontend-backend integration using HTML, CSS, JavaScript, and Bootstrap

Learned to test and debug APIs with Postman 

Future Enhancements

Add payment gateway integration

Implement order tracking and notifications

Add user roles for admin and restaurant management

Enable dynamic food recommendations based on user history

