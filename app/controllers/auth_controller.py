from flask import jsonify, request, make_response
import bcrypt
from app.models.user import User
from app.utils.auth import generate_token
from app import db

def register_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not username or not email or not password:
        return jsonify({'error': 'Missing username, email, or password'}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = User(
        username=username,
        email=email,
        user_image = data.get('user_image'),
        password=hashed_password.decode('utf-8'),
        address=data.get('address'),
        phone_number=data.get('phone_number'),
        status=data.get('status', 'active')
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify(message="User registered successfully"), 201

def login_user():
    auth = request.authorization
    email = auth.username
    password = auth.password

    print(email, password)

    if not auth or not email or not password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

    user = User.query.filter_by(email=email).first()
    
    if not user:
        return make_response('User not found', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

    if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({'error': 'Invalid email or password'}), 401

    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        token = generate_token(user.user_id)
        return jsonify({'token': token})
     
    return make_response('Not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})


def user_logout():
    pass