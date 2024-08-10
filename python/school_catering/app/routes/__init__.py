from app.routes.auth import auth_bp
from app.routes.parents import parents_bp
from app.routes.test import test_bp
from app.routes.dashboard import dashboard_bp
from app.routes.meal_giveout import meal_giveout_bp
from app.routes.menu import menu_bp
from app.routes.main import main_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(parents_bp)
    app.register_blueprint(test_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(meal_giveout_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(main_bp)