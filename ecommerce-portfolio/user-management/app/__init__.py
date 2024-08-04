from flask import Flask
from .models import db
from .routes import bp as user_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app/users.db'
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(user_routes)
    
    return app