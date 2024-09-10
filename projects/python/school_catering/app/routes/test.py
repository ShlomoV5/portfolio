from flask import Blueprint, jsonify, request
from app.models import db, User, Student, Meal, Absence, Menu, SpecialMeal, MealGiveout
from sqlalchemy import text, inspect
from sqlalchemy import func
from datetime import datetime, timedelta
import random
from faker import Faker

fake = Faker()

test_bp = Blueprint('test', __name__)


@test_bp.route('/test/tables', methods=['GET'])
def get_tables():
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    table_dict = {i + 1: table for i, table in enumerate(tables)}
    return jsonify({'tables': table_dict}), 200


@test_bp.route('/test/tables/<int:table_number>', methods=['GET'])
def get_latest_records(table_number):
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    if table_number < 1 or table_number > len(tables):
        return jsonify({'error': 'Invalid table number'}), 400

    table_name = tables[table_number - 1]
    query = text(f'SELECT * FROM {table_name} ORDER BY id DESC LIMIT 10')
    result = db.session.execute(query)
    records = [dict(row) for row in result.mappings()]
    return jsonify({'records': records}), 200


@test_bp.route('/test/state1', methods=['POST'])
def populate_db():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create meals
    meals = [
        Meal(name='Spaghetti', image_url='http://example.com/spaghetti.jpg'),
        Meal(name='Chicken Nuggets', image_url='http://example.com/nuggets.jpg'),
        Meal(name='Salad', image_url='http://example.com/salad.jpg')
    ]
    db.session.add_all(meals)
    db.session.commit()

    # Create regular menu
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    for i, meal in enumerate(meals):
        for day in weekdays:
            menu = Menu(weekday=day, meal_id=meal.id, is_default=(i == 0))
            db.session.add(menu)
    db.session.commit()

    # Create users and students
    for _ in range(10):  # 10 families
        user = User(
            name=fake.name(),
            email=fake.email(),
            password=fake.password(),
            status='active'
        )
        db.session.add(user)
        db.session.commit()

        for _ in range(fake.random_int(min=3, max=4)):  # 3 to 4 children per family
            student = Student(
                name=fake.first_name(),
                class_name=f'Class {fake.random_int(min=1, max=5)}',
                family_id=user.id
            )
            db.session.add(student)
    db.session.commit()

    # Create absences
    start_date = datetime.strptime('2024-01-01', '%Y-%m-%d')
    for _ in range(10):
        student_id = Student.query.order_by(func.random()).first().id
        date = start_date + timedelta(days=fake.random_int(min=0, max=13))
        absence = Absence(student_id=student_id, date=date)
        db.session.add(absence)
    db.session.commit()

    # Create special meals
    special_dates = ['2024-01-03', '2024-01-08', '2024-01-10']
    for date in special_dates:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        for meal in meals:
            special_meal = SpecialMeal(date=date_obj, meal_id=meal.id)
            db.session.add(special_meal)
    db.session.commit()

    return jsonify({'message': 'Database populated successfully'}), 201