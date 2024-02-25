from flask import Flask, jsonify, request,render_template

app = Flask(__name__)

data = {
    "products": [
        {"category": "Category 1", "id": "1", "name": "Apple", "price": 100},
        {"category": "Category 2", "id": 2, "name": "Banana", "price": 200},
        {"category": "Category 3", "id": 3, "name": "Grapes", "price": 300},
        {"category": "Category 4", "id": 4, "name": "Red Grapes", "price": 400},
        {"category": "Category 5", "id": 5, "name": "	Jackfruit", "price": 500},
        {"category": "Category 6", "id": 6, "name": "Mango", "price": 600},
        {"category": "Category 6", "id": 7, "name": "Orange", "price": 700},
        {"category": "Category 8", "id": 8, "name": "Tamarind", "price": 800},
        {"category": "Category 9", "id": 9, "name": "	Custard apple", "price": 900},
        {"category": "Category 10", "id": 10, "name": "Strawberry", "price": 1000},
    ]
}


@app.route("/")
def hello_world():
    return render_template("base.html")

@app.route('/product')
def product():
    return render_template('product.html')


@app.route("/product")
def return_json():
    return jsonify(data)


@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {username}'s profile"


@app.route("/id/<product_name>", methods=["GET"])
def get_product_id(product_name):
    for product in data["products"]:
        if product["name"] == product_name:
            return jsonify({"id": product["id"]})
    return jsonify({"error": "Product not found"})


@app.route("/products", methods=["GET"])
def get_products():
    products = []
    query_params = request.args
    category = query_params.get("category")
    name = query_params.get("name")
    product_id = query_params.get("id")
    if category:
        products = [
            product for product in data["products"] if product["category"] == category
        ]
    elif name:
        name = name.lower()
        products = [
            product for product in data["products"] if name in product["name"].lower()
        ]
    elif product_id:
        products = [
            product for product in data["products"] if str(product["id"]) == product_id
        ]
    else:
        products = data["products"]
    return jsonify({"products": products})


@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
