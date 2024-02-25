
# Product API

This is a simple Flask API that provides information about products.

## Endpoints

- `/product`: Returns all products.
- `/user/<username>`: Returns a user's profile.
- `/id/<product_name>`: Returns the ID of a product.
- `/products`: Returns products based on query parameters.

## Running the API

1. Install the required packages using `pip install -r requirements.txt`.
2. Run the API using `python app.py`.

## Query Parameters

- `category`: Filter products by category.
- `name`: Filter products by name (case-insensitive).
- `id`: Filter products by ID.

## Example

To get all products in "Category 1", you can use the following URL:

```
https://flask-api-oj9q.onrender.com

https://flask-api-oj9q.onrender.com/products
```

## Error Handling

If a product is not found, the API will return a JSON object with an error message.

## Note

This API is for demonstration purposes only and does not include any authentication or authorization mechanisms.
