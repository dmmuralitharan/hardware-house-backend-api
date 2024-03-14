from app import db

class Payment(db.Model):
    __tablename__ = 'payments'

    payment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    order_id = db.Column(db.Integer)
    payment_method = db.Column(db.String(100))
    payment_amount = db.Column(db.Numeric(10, 2))
    payment_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    payment_status = db.Column(db.Enum('success', 'failed'))
    transaction_id = db.Column(db.String(255))

    def serialize(self):
        return {
            'payment_id': self.payment_id,
            'user_id': self.user_id,
            'order_id': self.order_id,
            'payment_method': self.payment_method,
            'payment_amount': float(self.payment_amount) if self.payment_amount else None,
            'payment_date': self.payment_date,
            'payment_status': self.payment_status,
            'transaction_id': self.transaction_id
        }
