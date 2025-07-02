# 🛒 Sample Grocery Store

A simple, full‑stack grocery store management system built with **Python (Flask)** backend and a **frontend** using HTML, CSS, JavaScript, and Bootstrap.

---

## ✨ Features

- View / add / delete **products** with unit of measurement and pricing.
- Create **orders**: select multiple products, quantities, automatically calculate totals.
- Store orders and their line‑items in a **MySQL** database.
- Clean, responsive UI, powered by Bootstrap.

---

![hompage](https://github.com/user-attachments/assets/bff313d3-8e06-4f4c-9f0f-09792d2f1de4)


## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/diliboy/Sample-Grocery-Store-Python.git
cd Sample-Grocery-Store-Python
```

### 2. Configure backend environment

Create a database named grocery_store

Run provided SQL schema to create tables: products, uom, orders, order_details

Update sql_connection.py with your MySQL credentials.

###3. Run backend server
```bash
 python server.py
```

###4. Launch frontend
Use a simple static server, or VS Code Live Server:

```bash
cd ui
python -m http.server 5500
```
Open http://localhost:5500/index.html in your browser, or open via Live Server.
