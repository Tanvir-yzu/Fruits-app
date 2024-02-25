from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Determine the path to the JSON file
json_file_path = os.path.join(os.path.dirname(__file__), "data.json")

# Check if the file exists before trying to open it
if os.path.exists(json_file_path):
    # Load data from data.json file
    with open(json_file_path, "r") as f:
        data = json.load(f)
else:
    # Provide default data if file not found
    data = {"products": []}
    print(f"Warning: data.json not found at {json_file_path}")


@app.route("/")
def hello_world():
    return render_template("base.html")


@app.route("/product")
def product():
    return render_template("product.html", products=data["products"])


@app.route("/search", methods=["GET"])
def search_products():
    query_params = request.args
    name = query_params.get("name")
    if name:
        name = name.lower()
        # Filter products based on the search query
        search_results = [
            product for product in data["products"] if name in product["name"].lower()
        ]
    else:
        search_results = []  # Return empty list if no search query is provided
    return render_template("search_results.html", products=search_results)


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
