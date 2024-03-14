from flask import jsonify, request
from app import db
from app.models.category import Category

def get_categories():
    categories = Category.query.all()
    return jsonify([category.serialize() for category in categories]), 200

def get_category(category_id):
    category = Category.query.get(category_id)
    if category:
        return jsonify(category.serialize()), 200
    else:
        return jsonify({'message': 'Category not found'}), 404

def create_category():
    data = request.json
    new_category = Category(
        category_name=data['category_name'],
        category_description=data.get('category_description'),
        status=data.get('status')
    )
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category created successfully'}), 201

def update_category(category_id):
    data = request.json
    category = Category.query.get(category_id)
    if category:
        category.category_name = data.get('category_name', category.category_name)
        category.category_description = data.get('category_description', category.category_description)
        category.status = data.get('status', category.status)
        db.session.commit()
        return jsonify({'message': 'Category updated successfully'}), 200
    else:
        return jsonify({'message': 'Category not found'}), 404

def delete_category(category_id):
    category = Category.query.get(category_id)
    if category:
        db.session.delete(category)
        db.session.commit()
        return jsonify({'message': 'Category deleted successfully'}), 200
    else:
        return jsonify({'message': 'Category not found'}), 404
