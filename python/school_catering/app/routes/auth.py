from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session, flash
from app.models import db, User
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
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

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'error': 'Email address already in use'}), 400

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

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            if user.email == 'orly@orly.com':
                session['is_manager'] = True
                return redirect(url_for('dashboard.manager_dashboard'))
            else:
                session['is_manager'] = False
                return redirect(url_for('dashboard.parent_dashboard'))

        return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))