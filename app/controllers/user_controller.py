from flask import jsonify, request
from app.models.user import User
from app import db
import bcrypt


def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            'user_id': user.user_id,
            'username': user.username,
            'user_image': user.user_image,
            'email': user.email,
            'address': user.address,
            'phone_number': user.phone_number,
            'status': user.status,
            'registration_date': user.registration_date.strftime('%Y-%m-%d %H:%M:%S'),
            'last_login_date': user.last_login_date.strftime('%Y-%m-%d %H:%M:%S')
        }
        user_list.append(user_data)
    return jsonify(user_list)

def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        user_data = {
            'user_id': user.user_id,
            'username': user.username,
            'user_image': user.user_image,
            'email': user.email,
            'address': user.address,
            'phone_number': user.phone_number,
            'status': user.status,
            'registration_date': user.registration_date.strftime('%Y-%m-%d %H:%M:%S'),
            'last_login_date': user.last_login_date.strftime('%Y-%m-%d %H:%M:%S')
        }
        return jsonify(user_data)
    else:
        return jsonify({'error': 'User not found'}), 404

def create_user():
    user_data = request.json
    password = user_data.get('password')
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(
        username=user_data['username'],
        user_image=user_data.get('user_image'),
        email=user_data['email'],
        password=hashed_password.decode('utf-8'),
        address=user_data.get('address'),
        phone_number=user_data.get('phone_number'),
        status=user_data.get('status', 'active'),
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User created successfully"), 201

def update_user(user_id):
    user = User.query.get(user_id)
    user_data = request.json
    if user:
        user.username = user_data.get('username', user.username)
        user.user_image = user_data.get('user_image', user.user_image)
        user.password = user_data.get('password', user.password)
        user.email = user_data.get('email', user.email)
        user.address = user_data.get('address', user.address)
        user.phone_number = user_data.get('phone_number', user.phone_number)
        user.status = user_data.get('status', user.status)
        db.session.commit()
        return jsonify(message="User updated successfully")
    else:
        return jsonify({'error': 'User not found'}), 404

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify(message="User deleted successfully")
    else:
        return jsonify({'error': 'User not found'}), 404
