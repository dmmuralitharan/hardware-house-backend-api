import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/hardware_house'
    SQLALCHEMY_TRACK_MODIFICATIONS = False