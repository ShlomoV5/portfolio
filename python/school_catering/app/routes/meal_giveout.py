# meal_giveout.py
from flask import Blueprint, request, jsonify
from app.models import db, MealGiveout, Meal
from datetime import datetime

meal_giveout_bp = Blueprint('meal_giveout', __name__)

@meal_giveout_bp.route('/meal_giveout', methods=['POST'])
def giveout_meal():
    data = request.get_json()
    date_str = data.get('date')
    students = data.get('students')

    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format, use YYYY-MM-DD'}), 400

    for student_id in students:
        giveout = MealGiveout(student_id=student_id, date=date_obj)
        db.session.add(giveout)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Meals given out successfully.'}), 201

@meal_giveout_bp.route('/delete_giveout', methods=['DELETE'])
def delete_giveout():
    data = request.get_json()
    date_str = data.get('date')
    student_id = data.get('student_id')

    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format, use YYYY-MM-DD'}), 400

    giveout = MealGiveout.query.filter_by(student_id=student_id, date=date_obj).first()
    if not giveout:
        return jsonify({'error': 'Record not found'}), 404

    try:
        db.session.delete(giveout)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Meal giveout record deleted successfully.'}), 200

@meal_giveout_bp.route('/check_if_got', methods=['GET'])
def check_if_got():
    student_id = request.args.get('student_id')
    date_str = request.args.get('date')

    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format, use YYYY-MM-DD'}), 400

    giveout = MealGiveout.query.filter_by(student_id=student_id, date=date_obj).first()
    return jsonify({'got': giveout is not None}), 200

@meal_giveout_bp.route('/get_class_meals', methods=['GET'])
def get_class_meals():
    class_id = request.args.get('class_id')
    date_str = request.args.get('date')

    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format, use YYYY-MM-DD'}), 400

    meals = Meal.query.filter_by(class_id=class_id, date=date_obj).all()
    meal_list = [{'id': meal.id, 'name': meal.name} for meal in meals]
    return jsonify({'meals': meal_list}), 200
