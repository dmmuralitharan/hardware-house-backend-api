from app import db

class Cart(db.Model):
    __tablename__ = 'carts'

    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def serialize(self):
        return {
            'cart_id': self.cart_id,
            'user_id': self.user_id,
            'created_at': self.created_at,
            'product_id': self.product_id,
            'quantity': self.quantity
        }
