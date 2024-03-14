from app import db

class Category(db.Model):
    __tablename__ = 'categories'

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)
    category_description = db.Column(db.Text)
    status = db.Column(db.Enum('active', 'inactive', 'discontinued'), default='active')
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def serialize(self):
        return {
            'category_id': self.category_id,
            'category_name': self.category_name,
            'category_description': self.category_description,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
