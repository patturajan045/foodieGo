# FoodieGo – Full-Stack Food Ordering Application

FoodieGo is a full-stack web application that allows users to browse, order, and manage food items online. Built with **Flask, MongoDB, and modern frontend technologies**, it demonstrates end-to-end web application development, including user authentication, cart management, and order processing.

---

## Features

- User Management: Sign up, login, and manage profile information
- Customer Details: Store and manage customer addresses and contact information
- Cart & Orders: Add food items to the cart, update quantities, and place orders with delivery preferences
- RESTful APIs: Backend implemented using Flask and MongoEngine for database operations
- Database Design: MongoDB schemas for users, customers, carts, and orders with timestamps and UUIDs
- API Testing: All endpoints validated using Postman for reliability
- Frontend: Responsive design using HTML, CSS, JavaScript, and Bootstrap

---

## Tech Stack

- **Backend:** Python, Flask, MongoEngine  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Database:** MongoDB  
- **Tools:** Postman, Git  

---

## Project Structure

FoodieGo/
│
├─ app.py # Main Flask application
├─ models.py # MongoEngine models for User, Customer, Cart, and Order
├─ routes/ # Flask routes for API endpoints
├─ templates/ # HTML templates
├─ static/
│ ├─ css/ # Stylesheets
│ └─ js/ # JavaScript files
├─ README.md
└─ requirements.txt # Python dependencies 



---

## Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/FoodieGo.git
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

