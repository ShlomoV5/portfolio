from flask import Blueprint, request, render_template, redirect, url_for
from datetime import datetime
from app.models import db, MealDistribution, User

meal_distribution_bp = Blueprint('meal_distribution', __name__)

@meal_distribution_bp.route('/meal_distribution', methods=['GET', 'POST'])
def meal_distribution():
    if request.method == 'POST':
        class_id = request.form['class_id']
        student_meal_data = request.form.getlist('student_meal_data')

        for data in student_meal_data:
            student_id, status = data.split(':')
            distribution = MealDistribution.query.filter_by(student_id=student_id, date=datetime.today().date()).first()
            distribution.status = status
            db.session.commit()

        return redirect(url_for('meal_distribution.meal_distribution'))

    else:
        today = datetime.today().date()
        classes = get_classes()
        students_meal_data = get_students_meal_data()

        return render_template('meal_distribution.html', today=today, classes=classes, students_meal_data=students_meal_data)

def get_classes():
    return [
        {'id': 1, 'name': 'Class 1'},
        {'id': 2, 'name': 'Class 2'},
    ]

def get_students_meal_data():
    today = datetime.today().date()
    students_meal_data = []

    meal_distributions = MealDistribution.query.filter_by(date=today).all()
    for distribution in meal_distributions:
        student = User.query.get(distribution.student_id)
        meal = distribution.meal or distribution.special_meal
        students_meal_data.append({
            'student_id': student.id,
            'student_name': student.name,
            'meal_name': meal.name,
            'status': distribution.status
        })

    return students_meal_data
