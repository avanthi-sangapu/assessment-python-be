
import datetime
import bcrypt
from flask import jsonify
import jwt

from models import load_messages, load_users, save_messages, save_users

SECRET_KEY = "your-secret-key"
JSON_FILE = '../resources/messages.json'
USERS_FILE= '../resources/users.json'

# service logic for registering user
def register_user(data):
    username = data.get('username')
    email = data.get('email')
    role = data.get('role')
    password = data.get('password')
    
    users = load_users()
    new_id = max([u['id'] for u in users], default=0) + 1

    if not username or not email or not password:
        return jsonify({'error': 'Missing fields'}), 400

    # Check for existing username
    if any(user['username'] == username for user in users):
        return jsonify({'error': 'Username already registered'}), 400

    # Encrypt password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    user = {
        'id': new_id,
        'username': username,
        'email': email,
        'password': hashed_password,
        'role': role
    }
    users.append(user)
    save_users(users)

    return  jsonify({'message': 'User registered successfully',
                    'username' : username}), 201

# service logic for login user
def login_user(data):
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing fields'}), 400

    users = load_users()

    # Find user by email
    user = next((u for u in users if u['username'] == username), None)
    if not user:
        return jsonify({'error': 'Invalid email or password'}), 401

    # Check password
    if not bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        return jsonify({'error': 'Invalid email or password'}), 401
    
         # Create payload
    payload = {
        'username': user['username'],
        'role': user['role'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    # Encode token
    try:
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # PyJWT 2.x returns a string, older versions return bytes
        if isinstance(token, bytes):
            token = token.decode('utf-8')

    except Exception as e:
        return jsonify({'error': f'Failed to generate token: {str(e)}'}), 500
    return {
        'message': 'Login successful',
        'user_id': user['id'],
        'username': user['username'],
        'role': user['role'],
        'token': token,
        
    }

# service logic for adding new messages
def create_new_message(request):
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing or invalid Authorization header'}), 401

    token = auth_header.split(" ")[1]

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        data = request.get_json()
        messages = load_messages()
        new_id = max([m['id'] for m in messages], default=0) + 1
        new_msg = {
            'id': new_id,
            'userId': data['userId'],
            'text': data['text']
        }
        messages.append(new_msg)
        save_messages(messages)
        return jsonify({'message': 'Message added', 'data': new_msg}), 201
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401
    
# service logic for getting all messages
def get_all_messages(request):
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing or invalid Authorization header'}), 401

    token = auth_header.split(" ")[1]
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify(load_messages())

    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401



   

