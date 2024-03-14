from flask import Blueprint
from app.controllers.payment_controller import *
from app.utils.auth import token_required

payment_routes_bp = Blueprint('payment_routes_bp', __name__)

@payment_routes_bp.route('/payments', methods=['GET'])
def _get_all_payments():
    return get_all_payments()

@payment_routes_bp.route('/payments/<int:payment_id>', methods=['GET'])
def _get_payment_by_id(payment_id):
    return get_payment_by_id(payment_id)

@payment_routes_bp.route('/payments', methods=['POST'])
def _create_payment():
    return create_payment()

@payment_routes_bp.route('/payments/<int:payment_id>', methods=['PUT'])
def _update_payment(payment_id):
    return update_payment(payment_id)

@payment_routes_bp.route('/payments/<int:payment_id>', methods=['DELETE'])
def _delete_payment(payment_id):
    return delete_payment(payment_id)

