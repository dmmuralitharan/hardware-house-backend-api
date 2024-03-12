from flask import Blueprint
from app.controllers.product_controller import get_products, get_product, create_product, update_product, delete_product  

product_bp = Blueprint('product', __name__)
product_bp.route('/products')(get_products)
product_bp.route('/products/<int:product_id>', methods=['GET'])(get_product)
product_bp.route('/products', methods=['POST'])(create_product)
product_bp.route('/products/<int:product_id>', methods=['PUT'])(update_product)
product_bp.route('/products/<int:product_id>', methods=['DELETE'])(delete_product)
