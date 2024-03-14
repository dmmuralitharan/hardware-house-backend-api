from flask import Blueprint
from app.controllers.order_details_controller import *
from app.utils.auth import token_required

order_details_routes_bp = Blueprint('order_details_routes_bp', __name__)

@order_details_routes_bp.route('/order_details', methods=['GET'])
def _get_all_order_details():
    return get_all_order_details()

@order_details_routes_bp.route('/order_details/<int:order_detail_id>', methods=['GET'])
def _get_order_detail_by_id():
    return get_order_detail_by_id()
    
@order_details_routes_bp.route('/order_details', methods=['POST'])
def _create_order_detail():
    return create_order_detail()
    
@order_details_routes_bp.route('/order_details/<int:order_detail_id>', methods=['PUT'])
def _update_order_detail():
    return update_order_detail()
    
@order_details_routes_bp.route('/order_details/<int:order_detail_id>', methods=['DELETE'])
def _delete_order_detail():
    return delete_order_detail()
    
