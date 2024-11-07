from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample products data for testing
products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]

# Create a product: POST /products
@app.route('/products', methods=['POST'], strict_slashes=False)
def create_product():
    """Creates a new product"""
    product = request.get_json()  # Get the request body as JSON
    
    if not product:
        return jsonify({'error': 'Request body must be JSON'}), 400
    
    if 'name' not in product or 'price' not in product:
        return jsonify({'error': 'Missing name or price in request'}), 400
    
    # Assign a new id for the new product
    product['id'] = len(products) + 1  
    products.append(product)  # Add the new product to the list
    
    return jsonify(product), 201  # Return the new product and a 'created' status


# Retrieve all products: GET /products
@app.route('/products', methods=['GET'], strict_slashes=False)
def get_products():
    """Returns all products"""
    return jsonify(products)


# Retrieve a specific product: GET /products/<id>
@app.route('/products/<int:id>', methods=['GET'], strict_slashes=False)
def get_product(id):
    """Returns a specific product by id"""
    for product in products:
        if product['id'] == id:
            return jsonify(product)
    
    return jsonify({'error': 'Product not found'}), 404


# Update a specific product: PUT /products/<id>
@app.route('/products/<int:id>', methods=['PUT'], strict_slashes=False)
def update_product(id):
    """Updates a product by id"""
    updated_product = request.get_json()  # Get the request body as JSON
    
    if not updated_product:
        return jsonify({'error': 'Request body must be JSON'}), 400

    for product in products:
        if product['id'] == id:
            # Update product details with new data
            product.update(updated_product)
            return jsonify(product), 200
    
    return jsonify({'error': 'Product not found'}), 404


# Delete a product: DELETE /products/<id>
@app.route('/products/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete_product(id):
    """Deletes a product by id"""
    for product in products:
        if product['id'] == id:
            products.remove(product)
            return jsonify({'message': 'Product deleted successfully'}), 200
    
    return jsonify({'error': 'Product not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5070, debug=True)  # Start the Flask app

