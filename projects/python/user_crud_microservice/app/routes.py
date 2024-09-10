from flask import request, jsonify
from app import app, db
from app.models import User

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password_hash   
 = data.get('password_hash')  # Replace with actual password hashing

    user = User(username=username, email=email, password_hash=password_hash)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created   
 successfully'}), 201
