# parents.py
from flask import Blueprint, request, jsonify
from app.models import db, User, Absence, Student, Meal
from datetime import datetime

parents_bp = Blueprint('parents', __name__)

@parents_bp.route('/report_absence', methods=['POST'])
def report_absence():
    data = request.get_json()
    student_id = data.get('student_id')
    date_str = data.get('date')

    try:
        date_obj = datetime.strptime(date_str, '%Y%m%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format, use YYYYMMDD'}), 400

    absence = Absence(student_id=student_id, date=date_obj)

    try:
        db.session.add(absence)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Absence reported successfully.'}), 201

@parents_bp.route('/add_child', methods=['POST'])
def add_child():
    data = request.get_json()
    child_name = data.get('child_name')
    class_name = data.get('class')
    family_id = data.get('family_id')

    child = Child(name=child_name, class_name=class_name, family_id=family_id)

    try:
        db.session.add(child)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Child added successfully.'}), 201

@parents_bp.route('/show_menu', methods=['GET'])
def show_menu():
    meals = Meal.query.all()
    meal_list = [{'id': meal.id, 'name': meal.name, 'image_url': meal.image_url} for meal in meals]
    return jsonify({'meals': meal_list}), 200

@parents_bp.route('/choose_regular_meals', methods=['POST'])
def choose_regular_meals():
    data = request.get_json()
    choices = data.get('choices', {})  # Dictionary of day -> meal_id
    student_id = data.get('student_id')

    # Fetch default meals
    default_meals = Meal.query.filter_by(is_default=True).all()
    default_meals_dict = {meal.day: meal.id for meal in default_meals}

    # Apply choices or default meals
    for day, meal_id in choices.items():
        # Save meal choice for the day
        pass  # Implement saving logic

    # Apply default meal for days not chosen
    for day in range(1, 6):  # Assuming 5 days of the week
        if day not in choices:
            default_meal_id = default_meals_dict.get(day)
            if default_meal_id:
                # Save default meal choice for the day
                pass  # Implement saving logic

    return jsonify({'message': 'Meals selected successfully.'}), 201
