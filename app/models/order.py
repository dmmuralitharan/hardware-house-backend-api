from app import db

class Order(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    order_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    total_amount = db.Column(db.Numeric(10, 2))
    status = db.Column(db.Enum('pending', 'processing', 'shipped', 'delivered', 'cancelled', 'returned'))

    def serialize(self):
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'order_date': self.order_date,
            'total_amount': float(self.total_amount) if self.total_amount else None,
            'status': self.status
        }
