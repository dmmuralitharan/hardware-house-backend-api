from app.models.order import Order
from flask import jsonify, request
from app import db

def get_all_orders():
    orders = Order.query.all()
    return jsonify([order.serialize() for order in orders]), 200

def get_order_by_id(order_id):
    order = Order.query.get(order_id)
    if order:
        return jsonify(order.serialize()), 200
    else:
        return jsonify({'message': 'Order not found'}), 404

def create_order():
    data = request.json
    new_order = Order(
        user_id=data.get('user_id'),
        total_amount=data.get('total_amount'),
        status=data.get('status')
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully'}), 201

def update_order(order_id):
    data = request.json
    order = Order.query.get(order_id)
    if order:
        order.user_id = data.get('user_id', order.user_id)
        order.total_amount = data.get('total_amount', order.total_amount)
        order.status = data.get('status', order.status)
        db.session.commit()
        return jsonify({'message': 'Order updated successfully'}), 200
    else:
        return jsonify({'message': 'Order not found'}), 404

def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted successfully'}), 200
    else:
        return jsonify({'message': 'Order not found'}), 404
