from flask import Blueprint
from app.controllers.auth_controller import *

auth_routes_bp = Blueprint('auth_routes_bp', __name__)

@auth_routes_bp.route('/register', methods=['POST'])
def _register_user():
    return register_user()

@auth_routes_bp.route('/login', methods=['POST'])
def _login_user():
    return login_user()

@auth_routes_bp.route('/logout', methods=['POST'])
def _user_logout():
    return user_logout()