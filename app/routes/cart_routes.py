from flask import Blueprint
from app.controllers.cart_controller import *
from app.utils.auth import token_required

cart_routes_bp = Blueprint('cart_routes_bp', __name__)

@cart_routes_bp.route('/carts', methods=['GET'])
def _get_carts():
    return get_carts()

@cart_routes_bp.route('/carts/<int:cart_id>', methods=['GET'])
def _get_cart(cart_id):
    return get_cart(cart_id)

@cart_routes_bp.route('/carts', methods=['POST'])
def _create_cart():
    return create_cart()

@cart_routes_bp.route('/carts/<int:cart_id>', methods=['PUT'])
def _update_cart(cart_id):
    return update_cart(cart_id)

@cart_routes_bp.route('/carts/<int:cart_id>', methods=['DELETE'])
def _delete_cart(cart_id):
    return delete_cart(cart_id)
