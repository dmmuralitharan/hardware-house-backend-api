from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)

    from app.routes.product_routes import product_bp
    app.register_blueprint(product_bp, url_prefix='/api/v1')

    return app