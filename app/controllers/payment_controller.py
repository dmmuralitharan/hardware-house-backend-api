from app.models.payment import Payment
from flask import jsonify, request
from app import db

def get_all_payments():
    payments = Payment.query.all()
    return jsonify([payment.serialize() for payment in payments]), 200

def get_payment_by_id(payment_id):
    payment = Payment.query.get(payment_id)
    if payment:
        return jsonify(payment.serialize()), 200
    else:
        return jsonify({'message': 'Payment not found'}), 404

def create_payment():
    data = request.json
    new_payment = Payment(
        user_id=data.get('user_id'),
        order_id=data.get('order_id'),
        payment_method=data.get('payment_method'),
        payment_amount=data.get('payment_amount'),
        payment_status=data.get('payment_status'),
        transaction_id=data.get('transaction_id')
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({'message': 'Payment created successfully'}), 201

def update_payment(payment_id):
    data = request.json
    payment = Payment.query.get(payment_id)
    if payment:
        payment.user_id = data.get('user_id', payment.user_id)
        payment.order_id = data.get('order_id', payment.order_id)
        payment.payment_method = data.get('payment_method', payment.payment_method)
        payment.payment_amount = data.get('payment_amount', payment.payment_amount)
        payment.payment_status = data.get('payment_status', payment.payment_status)
        payment.transaction_id = data.get('transaction_id', payment.transaction_id)
        db.session.commit()
        return jsonify({'message': 'Payment updated successfully'}), 200
    else:
        return jsonify({'message': 'Payment not found'}), 404

def delete_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if payment:
        db.session.delete(payment)
        db.session.commit()
        return jsonify({'message': 'Payment deleted successfully'}), 200
    else:
        return jsonify({'message': 'Payment not found'}), 404
