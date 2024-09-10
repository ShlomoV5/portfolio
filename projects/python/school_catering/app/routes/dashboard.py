from flask import Blueprint, render_template, session, redirect, url_for
from app.models import User

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/manager_dashboard', methods=['GET'])
def manager_dashboard():
    if not session.get('is_manager'):
        return redirect(url_for('auth.login'))

    # Fetch relevant data for manager
    meals = Meal.query.all()
    return render_template('manager_dashboard.html', meals=meals)


@dashboard_bp.route('/parent_dashboard', methods=['GET'])
def parent_dashboard():
    if session.get('is_manager'):
        return redirect(url_for('auth.login'))

    # Fetch relevant data for parent
    user_id = session.get('user_id')
    student = Student.query.filter_by(parent_id=user_id).first()
    return render_template('parent_dashboard.html', student=student)