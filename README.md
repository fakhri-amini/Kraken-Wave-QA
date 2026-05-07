# Kraken Wave - QA Automation Project

Kraken Wave is a simple Flask web application integrated with MySQL and tested using QA automation tools such as Selenium WebDriver and Pytest.

This project is created as a QA Automation portfolio to demonstrate manual and automated testing skills.

---

## 🚀 Features

- Drink menu listing (Flask + MySQL)
- Add to cart system (session-based)
- Cart management (add / remove items)
- Checkout system with database integration
- Order storage in MySQL database

---

## 🧪 QA Testing Scope

### Selenium WebDriver
- UI testing (click buttons, navigation)
- Add to cart flow
- Checkout flow validation
- Cart validation after actions

### Pytest Framework
- Structured test cases
- Reusable test fixtures
- Automated test execution

---

## 🛠️ Tech Stack

- Python 3
- Flask
- MySQL
- Selenium WebDriver
- Pytest
- HTML (Jinja2 templates)

---

## 📁 Project Structure

Kraken-Wave/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── cart.html
│
├── tests/
│   └── test_app_pytest.py
│
└── README.md

---

## ⚙️ How to Run This Project

### 1. Clone Repository
git clone https://github.com/yourusername/kraken-wave-qa.git
cd kraken-wave-qa

---

### 2. Install Dependencies
pip install -r requirements.txt

---

### 3. Run Flask App
python app.py

Open in browser:
http://127.0.0.1:5000

---

### 4. Run Tests (Pytest)
pytest -v

---

## 🧪 Test Scenarios

- Home page loads successfully
- Add item to cart
- Remove item from cart
- Checkout process works correctly
- Cart resets after checkout

---

## 🎯 Learning Goals

- QA Automation fundamentals
- Selenium WebDriver usage
- Pytest framework structure
- Flask web application testing
- End-to-end testing flow

---

## 👨‍💻 Author

QA Automation portfolio project for learning and job application purposes.

---

## 📌 Notes

- Make sure MySQL server is running
- Update database credentials in app.py
- Run Flask app before running Selenium tests
