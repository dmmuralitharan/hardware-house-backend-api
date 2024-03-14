from flask import Blueprint
from app.controllers.product_controller import *
from app.utils.auth import token_required

product_routes_bp = Blueprint('product_routes_bp', __name__)

@product_routes_bp.route('/products')
def _get_products():
    return get_products()

@product_routes_bp.route('/products/<int:product_id>', methods=['GET'])
def _get_product(product_id):
    return get_product(product_id)

@product_routes_bp.route('/products', methods=['POST'])
@token_required
def _create_product(current_user):
    return create_product()

@product_routes_bp.route('/products/<int:product_id>', methods=['PUT'])
@token_required
def _update_product(current_user, product_id):
    return update_product(product_id)

@product_routes_bp.route('/products/<int:product_id>', methods=['DELETE'])
@token_required
def _delete_product(current_user, product_id):
    return delete_product(product_id)
