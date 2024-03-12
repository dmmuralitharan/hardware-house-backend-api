from app import db

class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    quantity_available = db.Column(db.Integer)
    product_image = db.Column(db.String(255))
    category_id = db.Column(db.Integer)
    status = db.Column(db.Enum('active', 'inactive', 'discontinued'), default='active')
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return '<Product %r>' % self.product_name

    def serialize(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'description': self.description,
            'price': float(self.price) if self.price is not None else None,
            'quantity_available': self.quantity_available,
            'product_image': self.product_image,
            'category_id': self.category_id,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
