from flask import Blueprint
from app.controllers.user_controller import *
from app.utils.auth import token_required

user_routes_bp = Blueprint('user_routes_bp', __name__)

@user_routes_bp.route('/users', methods=['GET'])
@token_required
def _get_users(current_user):
    return get_users()

@user_routes_bp.route('/users/<int:user_id>', methods=['GET'])
def _get_user(user_id):
    return get_user(user_id)

@user_routes_bp.route('/users', methods=['POST'])
@token_required
def _create_user(current_user):
    return create_user()

@user_routes_bp.route('/users/<int:user_id>', methods=['PUT'])
@token_required
def _update_user(current_user, user_id):
    return update_user(user_id)

@user_routes_bp.route('/users/<int:user_id>', methods=['DELETE'])
@token_required
def _delete_user(current_user, user_id):
    return delete_user(user_id)