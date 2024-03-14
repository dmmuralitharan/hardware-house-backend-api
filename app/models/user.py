from app import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    user_image = db.Column(db.String(255))
    email = db.Column(db.String(100))
    password = db.Column(db.String(255))
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    status = db.Column(db.String(20))
    registration_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    last_login_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return '<User %r>' % self.username
