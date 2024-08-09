from flask import Blueprint, request, jsonify
from app.models import db, User
from app.utils import validate_email, validate_password, hash_password, generate_verification_token, save_token_to_db, send_verification_email

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    if not validate_email(email):
        return jsonify({'message': 'Invalid email'}), 400

    if not validate_password(password):
        return jsonify({'message': 'Invalid password'}), 400

    hashed_password = hash_password(password)
    user = User(name=name, email=email, password=hashed_password, status='pending')
    db.session.add(user)
    db.session.commit()

    token = generate_verification_token(email)
    save_token_to_db(user, token)
    verification_link = f'http://localhost:5000/verify/{token}'
    send_verification_email(email, verification_link)

    return jsonify({'message': 'User created successfully. Please check your email to verify your account.'}), 201

@auth_bp.route('/verify/<token>', methods=['GET'])
def verify_email(token):
    user = User.query.filter_by(token=token).first()

    if user:
        user.status = 'active'
        user.token = None
        db.session.commit()
        return jsonify({'message': 'Email verified successfully!'}), 200
    else:
        return jsonify({'message': 'Invalid or expired token'}), 400