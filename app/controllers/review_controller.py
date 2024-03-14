from app.models.review import Review
from flask import jsonify, request
from app import db

def get_reviews():
    reviews = Review.query.all()
    return jsonify([review.serialize() for review in reviews]), 200

def get_review(review_id):
    review = Review.query.get(review_id)
    if review:
        return jsonify(review.serialize()), 200
    else:
        return jsonify({'message': 'Review not found'}), 404

def create_review():
    data = request.json

    new_review = Review(
        product_id=data['product_id'],
        user_id=data['user_id'],
        rating=data['rating'],
        review_text=data['review_text']
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review created successfully'}), 201

def update_review(review_id):
    data = request.json

    review = Review.query.get(review_id)
    if review:
        review.product_id = data.get('product_id', review.product_id)
        review.user_id = data.get('user_id', review.user_id)
        review.rating = data.get('rating', review.rating)
        review.review_text = data.get('review_text', review.review_text)
        db.session.commit()
        return jsonify({'message': 'Review updated successfully'}), 200
    else:
        return jsonify({'message': 'Review not found'}), 404

def delete_review(review_id):
    review = Review.query.get(review_id)

    if review:
        db.session.delete(review)
        db.session.commit()
        return jsonify({'message': 'Review deleted successfully'}), 200
    else:
        return jsonify({'message': 'Review not found'}), 404
