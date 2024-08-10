from flask import Blueprint, request, jsonify
from app.models import db, Meal, Menu, SpecialMeal

menu_bp = Blueprint('menu', __name__)


@menu_bp.route('/show_meals', methods=['GET'])
def show_meals():
    meals = Meal.query.all()
    meals_list = [{'id': meal.id, 'name': meal.name, 'image_url': meal.image_url} for meal in meals]
    return jsonify({'meals': meals_list}), 200


@menu_bp.route('/add_meals', methods=['POST'])
def add_meals():
    data = request.get_json()
    name = data.get('name')
    image_url = data.get('image_url', '')  # Default to empty string if image_url is not provided

    if not name:
        return jsonify({'error': 'Meal name is required'}), 400

    meal = Meal(name=name, image_url=image_url)
    db.session.add(meal)
    db.session.commit()
    return jsonify({'message': 'Meal added successfully'}), 201


@menu_bp.route('/show_regular_menu', methods=['GET'])
def show_regular_menu():
    menu = Menu.query.all()
    menu_list = [{'day': item.day, 'meal': item.meal.name} for item in menu]
    return jsonify({'regular_menu': menu_list}), 200


@menu_bp.route('/edit_regular_menu', methods=['PUT'])
def edit_regular_menu():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    for day, meals in data.items():
        # Delete existing menu for the day
        Menu.query.filter_by(day=day).delete()

        # Add new meals for the day
        for meal_id in meals:
            menu_item = Menu(day=day, meal_id=meal_id)
            db.session.add(menu_item)

    db.session.commit()
    return jsonify({'message': 'Regular menu updated successfully'}), 200


@menu_bp.route('/show_week_menu', methods=['GET'])
def show_week_menu():
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    special_meals = SpecialMeal.query.filter(SpecialMeal.date.between(today, end_date)).all()

    week_menu = []
    for day in range(7):
        current_date = today + timedelta(days=day)
        special_meal = next((sm for sm in special_meals if sm.date == current_date), None)
        if special_meal:
            week_menu.append({'date': current_date.strftime('%Y-%m-%d'), 'meal': special_meal.meal.name})
        else:
            weekday = current_date.strftime('%A')
            regular_meal = Menu.query.filter_by(day=weekday).first()
            if regular_meal:
                week_menu.append({'date': current_date.strftime('%Y-%m-%d'), 'meal': regular_meal.meal.name})
            else:
                week_menu.append({'date': current_date.strftime('%Y-%m-%d'), 'meal': 'No meal available'})

    return jsonify({'week_menu': week_menu}), 200


@menu_bp.route('/add_special_meal', methods=['POST'])
def add_special_meal():
    data = request.get_json()
    date_str = data.get('date')
    meal_ids = data.get('meal_ids')

    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format, use YYYY-MM-DD'}), 400

    for meal_id in meal_ids:
        special_meal = SpecialMeal(date=date_obj, meal_id=meal_id)
        db.session.add(special_meal)

    db.session.commit()
    return jsonify({'message': 'Special meal added successfully'}), 201
