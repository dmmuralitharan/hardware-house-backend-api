from app.models.cart import Cart
from flask import jsonify, request
from app import db

def get_carts():
    carts = Cart.query.all()
    return jsonify([cart.serialize() for cart in carts]), 200

def get_cart(cart_id):
    cart = Cart.query.get(cart_id)
    if cart:
        return jsonify(cart.serialize()), 200
    else:
        return jsonify({'message': 'Cart not found'}), 404

def create_cart():
    data = request.json
    new_cart = Cart(
        user_id=data['user_id'],
        product_id=data['product_id'],
        quantity=data['quantity']
    )
    db.session.add(new_cart)
    db.session.commit()
    return jsonify({'message': 'Cart created successfully'}), 201

def update_cart(cart_id):
    data = request.json
    cart = Cart.query.get(cart_id)
    if cart:
        cart.user_id = data.get('user_id', cart.user_id)
        cart.product_id = data.get('product_id', cart.product_id)
        cart.quantity = data.get('quantity', cart.quantity)
        db.session.commit()
        return jsonify({'message': 'Cart updated successfully'}), 200
    else:
        return jsonify({'message': 'Cart not found'}), 404

def delete_cart(cart_id):
    cart = Cart.query.get(cart_id)
    if cart:
        db.session.delete(cart)
        db.session.commit()
        return jsonify({'message': 'Cart deleted successfully'}), 200
    else:
        return jsonify({'message': 'Cart not found'}), 404
