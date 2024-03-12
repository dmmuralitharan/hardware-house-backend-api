from flask import Blueprint, jsonify, request
from app.models.product import Product
from app import db

def get_products():
    products = Product.query.all()
    result = []
    for product in products:
        result.append(product.serialize())
    return jsonify(result)

def get_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product.serialize())

def create_product():
    data = request.json
    product = Product(
        product_name=data['product_name'],
        description=data.get('description'),
        price=data.get('price'),
        quantity_available=data.get('quantity_available'),
        product_image=data.get('product_image'),
        category_id=data.get('category_id'),
        status=data.get('status', 'active')
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

def update_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    data = request.json
    product.product_name = data.get('product_name', product.product_name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.quantity_available = data.get('quantity_available', product.quantity_available)
    product.product_image = data.get('product_image', product.product_image)
    product.category_id = data.get('category_id', product.category_id)
    product.status = data.get('status', product.status)
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

def delete_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})