from app import db

class Review(db.Model):
    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float)
    review_text = db.Column(db.Text)
    review_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    def serialize(self):
        return {
            'review_id': self.review_id,
            'product_id': self.product_id,
            'user_id': self.user_id,
            'rating': self.rating,
            'review_text': self.review_text,
            'review_date': self.review_date
        }
