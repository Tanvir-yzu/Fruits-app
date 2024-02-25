from flask import Flask, jsonify,request

app = Flask(__name__)

data = {
  "products": [
    {
      "category": "Category 1",
      "id": "1",
      "name": "Product 1",
      "price": 100
    },
    {
      "category": "Category 2",
      "id": 2,
      "name": "Product 2",
      "price": 200
    },
    {
      "category": "Category 3",
      "id": 3,
      "name": "Product 3",
      "price": 300
    },
    {
      "category": "Category 4",
      "id": 4,
      "name": "Product 4",
      "price": 400
    },
    {
      "category": "Category 5",
      "id": 5,
      "name": "Product 5",
      "price": 500
    },
    {
      "category": "Category 6",
      "id": 6,
      "name": "Product 6",
      "price": 600
    },
    {
      "category": "Category 7",
      "id": 7,
      "name": "Product 7",
      "price": 700
    },
    {
      "category": "Category 8",
      "id": 8,
      "name": "Product 8",
      "price": 800
    },
    {
      "category": "Category 9",
      "id": 9,
      "name": "Product 9",
      "price": 900
    },
    {
      "category": "Category 10",
      "id": 10,
      "name": "Product 10",
      "price": 1000
    }
  ]
}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/product")
def return_json():
    return jsonify(data)

@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {username}'s profile"

@app.route('/id/<product_name>', methods=['GET'])
def get_product_id(product_name):
    for product in data["products"]:
        if product["name"] == product_name:
            return jsonify({"id": product["id"]})
    return jsonify({"error": "Product not found"})

@app.route('/products', methods=['GET'])
def get_products():
    products = []
    query_params = request.args
    if 'category' in query_params:
        category = query_params['category']
        for product in data['products']:
            if product['category'] == category:
                products.append(product)
    elif 'name' in query_params:
        name = query_params['name']
        for product in data['products']:
            if name.lower() in product['name'].lower():
                products.append(product)
    elif 'id' in query_params:
        product_id = query_params['id']
        for product in data['products']:
            if str(product['id']) == product_id:
                products.append(product)
    else:
        products = data['products']
    return jsonify({'products': products})

if __name__ == '__main__':
    app.run(debug=True)
