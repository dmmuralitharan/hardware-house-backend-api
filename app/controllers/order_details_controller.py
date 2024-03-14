from app.models.order_details import OrderDetail
from flask import jsonify, request
from app import db

def get_all_order_details():
    order_details = OrderDetail.query.all()
    return jsonify([order_detail.serialize() for order_detail in order_details]), 200

def get_order_detail_by_id(order_detail_id):
    order_detail = OrderDetail.query.get(order_detail_id)
    if order_detail:
        return jsonify(order_detail.serialize()), 200
    else:
        return jsonify({'message': 'Order Detail not found'}), 404

def create_order_detail():
    data = request.json
    new_order_detail = OrderDetail(
        order_id=data.get('order_id'),
        product_id=data.get('product_id'),
        quantity=data.get('quantity'),
        unit_price=data.get('unit_price')
    )
    db.session.add(new_order_detail)
    db.session.commit()
    return jsonify({'message': 'Order Detail created successfully'}), 201

def update_order_detail(order_detail_id):
    data = request.json
    order_detail = OrderDetail.query.get(order_detail_id)
    if order_detail:
        order_detail.order_id = data.get('order_id', order_detail.order_id)
        order_detail.product_id = data.get('product_id', order_detail.product_id)
        order_detail.quantity = data.get('quantity', order_detail.quantity)
        order_detail.unit_price = data.get('unit_price', order_detail.unit_price)
        db.session.commit()
        return jsonify({'message': 'Order Detail updated successfully'}), 200
    else:
        return jsonify({'message': 'Order Detail not found'}), 404

def delete_order_detail(order_detail_id):
    order_detail = OrderDetail.query.get(order_detail_id)
    if order_detail:
        db.session.delete(order_detail)
        db.session.commit()
        return jsonify({'message': 'Order Detail deleted successfully'}), 200
    else:
        return jsonify({'message': 'Order Detail not found'}), 404
