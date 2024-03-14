from flask import Blueprint
from app.controllers.order_controller import *
from app.utils.auth import token_required

order_routes_bp = Blueprint('order_routes_bp', __name__)

@order_routes_bp.route('/orders', methods=['GET'])
def _get_all_orders():
    return get_all_orders()

@order_routes_bp.route('/orders/<int:order_id>', methods=['GET'])
def _get_order_by_id(order_id):
    return get_order_by_id(order_id)

@order_routes_bp.route('/orders', methods=['POST'])
def _create_order():
    return create_order()

@order_routes_bp.route('/orders/<int:order_id>', methods=['PUT'])
def _update_order(order_id):
    return update_order(order_id)

@order_routes_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def _delete_order(order_id):
    return delete_order(order_id)

