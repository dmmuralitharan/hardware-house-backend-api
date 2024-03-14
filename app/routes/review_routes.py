from flask import Blueprint
from app.controllers.review_controller import *
from app.utils.auth import token_required

review_routes_bp = Blueprint('review_routes_bp', __name__)

@review_routes_bp.route('/reviews', methods=['GET'])
def _get_reviews():
    return _get_reviews()

@review_routes_bp.route('/reviews/<int:review_id>', methods=['GET'])
def _get_review(review_id):
    return get_review(review_id)

@review_routes_bp.route('/reviews', methods=['POST'])
def _create_review():
    return create_review()

@review_routes_bp.route('/reviews/<int:review_id>', methods=['PUT'])
def _update_review(review_id):
    return update_review(review_id)

@review_routes_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
def _delete_review(review_id):
    return delete_review(review_id)

