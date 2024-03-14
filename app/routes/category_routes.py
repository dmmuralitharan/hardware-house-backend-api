from flask import Blueprint
from app.controllers.category_controller import *
from app.utils.auth import token_required

category_routes_bp = Blueprint('category_routes_bp', __name__)

@category_routes_bp.route('/categories', methods=['GET'])
def _get_categories():
    return get_categories()

@category_routes_bp.route('/categories/<int:category_id>', methods=['GET'])
def _get_category(category_id):
    return get_category(category_id)

@category_routes_bp.route('/categories', methods=['POST'])
@token_required
def _create_category(current_user):
    return create_category()

@category_routes_bp.route('/categories/<int:category_id>', methods=['PUT'])
@token_required
def _update_category(current_user, category_id):
    return update_category(category_id)

@category_routes_bp.route('/categories/<int:category_id>', methods=['DELETE'])
@token_required
def _delete_category(current_user, category_id):
    return delete_category(category_id)
