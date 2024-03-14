from app import db

class OrderDetail(db.Model):
    __tablename__ = 'order_details'

    order_detail_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Numeric(10, 2))

    def serialize(self):
        return {
            'order_detail_id': self.order_detail_id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'unit_price': float(self.unit_price) if self.unit_price else None
        }
