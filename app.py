from flask import Flask, render_template, session, redirect, url_for, request, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret123"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root@35",
    database="Kraken_Wave"
)

def get_drinks():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM drinks")
    drinks = cursor.fetchall()
    return drinks

@app.route("/")
def home():
    drinks = get_drinks()
    cart = session.get("cart", {})
    cart_count = sum(cart.values()) if isinstance(cart, dict) else 0
    return render_template("index.html", drinks=drinks, cart_count=cart_count)

@app.route("/add/<int:id>/<source>")
def add_to_cart(id, source):
    cart = session.get("cart", {})
    if isinstance(cart, list):
        cart = {}

    id_str = str(id)

    if id_str in cart:
        cart[id_str] += 1
    else:
        cart[id_str] = 1

    session["cart"] = cart
    session.modified = True

    return redirect(url_for(source))

@app.route("/remove/<int:id>")
def remove_from_cart(id):
    cart = session.get("cart", {})

    id_str = str(id)

    if id_str in cart:
        del cart[id_str]

    session["cart"] = cart
    session.modified = True

    return redirect(url_for("cart"))

@app.route("/cart")
def cart():
    drinks = get_drinks()
    cart = session.get("cart", {})

    cart_items = []
    total = 0

    for id_str, qty in cart.items():
        for drink in drinks:
            if drink["id"] == int(id_str):
                subtotal = drink["price"] * qty
                total += subtotal

                cart_items.append({
                "id":drink["id"],
                "name":drink["name"],
                "price":drink["price"],
                "qty":qty,
                "subtotal":subtotal

            })

    return render_template("cart.html", cart_items=cart_items, total=total)

@app.route("/checkout")
def checkout():
    cart = session.get("cart", {})

    if not cart:
        return "Cart kosong"

    drinks = get_drinks()
    cursor = db.cursor()
    total = 0

    for id_str, qty in cart.items():
        for drink in drinks:
            if drink["id"] == int(id_str):
                total += drink["price"] * qty

    cursor.execute("INSERT INTO orders(total) VALUES (%s)", (total,))
    order_id = cursor.lastrowid

    for id_str, qty in cart.items():
        for drink in drinks:
            if drink["id"] == int(id_str):
                cursor.execute(
                    "INSERT INTO order_items(order_id, drink_id, qty) VALUES (%s,%s,%s)",
                    (order_id, drink["id"], qty)
                )

    db.commit()
    session["cart"] = {}
    return "Checkout berhasil"


# API ROUTES
# API GET DRINKS
@app.route("/api/drinks", methods=["GET"])
def api_get_drinks():
    drinks = get_drinks()
    return jsonify(drinks)


# API ADD TO CART
@app.route("/api/cart/add", methods=["POST"])
def api_add_to_cart():
    data = request.get_json()

    if not data or "id" not in data:
        return jsonify({"error": "ID is required"}), 400

    if not isinstance(data["id"], int):
        return jsonify({"error": "ID must be integer"}), 400

    drink_id = str(data["id"])
    cart = session.get("cart", {})

    if drink_id in cart:
        cart[drink_id] += 1
    else:
        cart[drink_id] = 1

    session["cart"] = cart
    session.modified = True

    return jsonify({
        "message": "Item added",
        "cart": cart
    })


# API CHECKOUT
@app.route("/api/checkout", methods=["POST"])
def api_checkout():
    cart = session.get("cart", {})
    drinks = get_drinks()

    cursor = db.cursor()
    total = 0

    for id_str, qty in cart.items():
        for drink in drinks:
            if drink["id"] == int(id_str):
                total += drink["price"] * qty

    cursor.execute("INSERT INTO orders(total) VALUES (%s)", (total,))
    order_id = cursor.lastrowid

    for id_str, qty in cart.items():
        for drink in drinks:
            if drink["id"] == int(id_str):
                cursor.execute(
                    "INSERT INTO order_items(order_id, drink_id, qty) VALUES (%s,%s,%s)",
                    (order_id, drink["id"], qty)
                )

    db.commit()
    session["cart"] = {}

    return jsonify({
        "message": "Checkout berhasil",
        "order_id": order_id,
        "total": total
    })

if __name__=="__main__":
    app.run(debug=True)