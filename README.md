# 🕯️ Cadenza — Flask E-Commerce Fragrance Store

**Cadenza** is a QUT university project (IFN564, Rapid Web Development) designed as an interactive online fragrance store built using **Flask**, **Python**, and **SQLite**. It allows users to browse a product catalogue (candles and colognes), add and remove items from a cart, and complete a purchase flow with form validation.

---

## 🛍️ Key Features

- **Home Page** – Clean landing page introducing the store  
- **Products Page** – Filterable by category (candles/colognes/scent notes)  
- **Checkout Page** – Form with validation to simulate order processing  
- Add and remove items from cart dynamically  
- Uses SQLite for product, cart, and transaction handling  
- Custom 404 and 500 error templates  
- Cart, profits, and orders handled through backend logic

---

## 🧰 Tech Stack

- **Python 3.10+**
- **Flask**
- **Jinja2 Templating**
- **SQLite**
- **HTML / CSS (custom + Bootstrap)**

---

## 🗂️ Project Structure

```plaintext
cadenza/
├── static/
│   ├── css/style.css
│   └── img/                # Product & banner assets
├── templates/
│   ├── base.html           # Template layout
│   ├── index.html          # Home page
│   ├── shop.html           # Product listings
│   ├── product.html        # Individual product details
│   ├── basket.html         # Shopping cart
│   ├── checkout.html       # Checkout form
│   ├── 404.html / 500.html # Error pages
├── instance/
│   └── cadenza.sqlite      # SQLite DB
├── forms.py                # WTForms: checkout and validation
├── models.py               # ORM models for product, order, transaction
├── views.py                # App routes and logic
├── run.py                  # Entry point
└── __init__.py             # App factory
```

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cadenza.git
cd cadenza
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the App

```bash
python run.py
```

Then open `http://127.0.0.1:5000/` in your browser.

---

## 🧪 Project Purpose

This application was developed as part of a university assignment focused on:

- Understanding CRUD operations with databases
- Building dynamic web interfaces with server-side rendering
- Managing user interaction in e-commerce flows

---

## 📄 License

This project is provided for educational purposes under the [MIT License](LICENSE).

---

