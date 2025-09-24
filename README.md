# 👟 Shoes House – E-Commerce Shoe Store

**Shoes House**, Shoes House is an e-commerce platform developed using Django and Bootstrap.
Users can browse shoes, add them to cart, place orders, and manage their accounts.
Visually elegant, structurally solid! 😎💼

---

## ✨ Features

### 👤 User Operations
- ✅ Registration & Login system
- ✅ Şifre doğrulama & güncelleme
- ✅ Edit profile information
- ✅ Secure logout

### 👟 Product Management
- ✅ Listing by category (Men / Women / Kids)
- ✅ Filtering (color, size, ankle height, etc.)
- ✅ Add/remove from cart
- ✅ Order history & details

### 💳 Payment System
- ✅ Credit card payment
- ✅ Edit billing address
- ✅ Order summary

### ✉️ Contact
- ✅ Customer message system
- ✅ Contact form

---

## 🖼️ Screenshots

### 🏠 Home Page  
Categorized products, campaigns, and featured shoes.

![Ana Sayfa](screenshots/home.png)
![Ana Sayfa](screenshots/home2.png)
![Ana Sayfa](screenshots/home3.png)

### 🔐 Login Page  
User login form with email and password.

![Giriş Sayfası](screenshots/login.png)

### 📝 Register Page  
New user registration screen.

![Kayıt Sayfası](screenshots/register.png)

### 🛒 Cart  
Shows products added to cart and total amount.

![Ana Sayfa](screenshots/card.png)

### 💳 Payment Page  
Billing information and credit card form.

![Ana Sayfa](screenshots/payment.png)

### 👤 Profile Page
User information, address, and password management.

![Ana Sayfa](screenshots/profile.png)

### 🔎 Search 
Page allowing product search by name.
> 🔍 Users can search by product name.

![Ana Sayfa](screenshots/search.png)

### 📦 Order History (My Orders)  
Page listing user's previous orders.
> 📋 Displays order number, date, total amount, and status.

![Ana Sayfa](screenshots/orders.png)

### 👟 Product Detail Page
Large image, description, price, and add-to-cart button for selected product.  
> 🧾 Includes size and color information. Purchasing users can leave reviews and ratings.

![Ana Sayfa](screenshots/porduct-detail.png)

### 📬 Contact  
Customer message form and contact information.

![Ana Sayfa](screenshots/home4.png)

### 🛠️ Admin Panel  
Administrator screen for managing products, orders, and users.

![Ana Sayfa](screenshots/admin.png)


---

## ⚙️ Installation

Clone the repository
   
- git clone https://github.com/GoktugGok/Shoes_Shop.git

Enter the project folder
   
- cd Shoes_Shop

Create virtual environment
   
- python -m venv env

Activate environment
   
- Windows:
venv\Scripts\activate

- Mac/Linux:
source venv/bin/activate

Install requirements
   
- pip install -r requirements.txt

Create database
   
- python manage.py migrate

(Optional) Create admin user
   
- python manage.py createsuperuser

Run server
   
- python manage.py runserver



