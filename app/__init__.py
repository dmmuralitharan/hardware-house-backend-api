from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)

    from app.routes.auth_routes import auth_routes_bp
    from app.routes.user_routes import user_routes_bp
    from app.routes.category_routes import category_routes_bp
    from app.routes.product_routes import product_routes_bp
    from app.routes.review_routes import review_routes_bp
    
    app.register_blueprint(auth_routes_bp, url_prefix='/api/v1')
    app.register_blueprint(user_routes_bp, url_prefix='/api/v1')
    app.register_blueprint(category_routes_bp, url_prefix='/api/v1')
    app.register_blueprint(product_routes_bp, url_prefix='/api/v1')
    app.register_blueprint(review_routes_bp, url_prefix='/api/v1')

    return app