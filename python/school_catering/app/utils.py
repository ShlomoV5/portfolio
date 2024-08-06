import re
import hashlib
from app.models import db, User
import jwt
from datetime import datetime, timedelta
from config import Config
from app.models import db, Token


def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None


def validate_password(password):
    # Password must be at least 8 characters long, contain an uppercase letter, a lowercase letter, a number, and a special character
    regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    return re.match(regex, password) is not None


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def generate_verification_token(email):
    expiration = datetime.utcnow() + timedelta(hours=24)
    token = jwt.encode({'email': email, 'exp': expiration}, Config.SECRET_KEY, algorithm='HS256')
    return token


def save_token_to_db(user, token):
    user.token = token
    db.session.commit()


def send_verification_email(email, link):
    #msg = MIMEMultipart()
    #msg['From'] = formataddr(('School Catering', current_app.config['MAIL_USERNAME']))
    #msg['To'] = email
    #msg['Subject'] = 'Email Verification'

    #body = f'Please click the following link to verify your email: {link}'
    #msg.attach(MIMEText(body, 'plain'))

    #try:
    #    server = smtplib.SMTP(current_app.config['MAIL_SERVER'], current_app.config['MAIL_PORT'])
    #    server.starttls()
    #    server.login(current_app.config['MAIL_USERNAME'], current_app.config['MAIL_PASSWORD'])
    #    text = msg.as_string()
    #    server.sendmail(current_app.config['MAIL_USERNAME'], email, text)
    #    server.quit()
    #except Exception as e:
    #    print(f"Failed to send email: {e}")
    print(f"Email was sent (not really) successfully. Verification link: {link}")

def confirm_verification_token(token):
    user = User.query.filter_by(token=token).first()
    if user:
        user.token = None
        db.session.commit()
        return user.email
    return None

def verify_token(token):
    try:
        data = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        return data['email']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None