from flask import Blueprint, render_template
from datetime import datetime
from app.models import Meal, SpecialMeal, MealDistribution, Absence

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
def dashboard():
    today = datetime.today().date()
    weekday = today.weekday()

    regular_meals = Meal.query.filter_by(weekday=weekday).all()
    special_meal = SpecialMeal.query.filter_by(date=today).first()

    meal_count = MealDistribution.query.filter_by(date=today).count()
    away_count = Absence.query.filter_by(date=today).count()
    kids_away = Absence.query.filter_by(date=today).all()
    given_count = MealDistribution.query.filter_by(date=today, status='given').count()

    return render_template('dashboard.html', regular_meals=regular_meals, special_meal=special_meal, meal_count=meal_count, away_count=away_count, kids_away=kids_away, given_count=given_count)
