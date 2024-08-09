from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    token = db.Column(db.String(200), nullable=True)
    tokens = db.relationship('Token', back_populates='user', cascade='all, delete-orphan')
    meal_distributions = db.relationship('MealDistribution', back_populates='student', cascade='all, delete-orphan')
    absences = db.relationship('Absence', back_populates='student', cascade='all, delete-orphan')


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(200), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship('User', back_populates='tokens')

User.tokens = db.relationship('Token', back_populates='user', cascade='all, delete-orphan')

class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    students = db.relationship('Student', backref='family', lazy=True, cascade='all, delete-orphan')

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    family_id = db.Column(db.Integer, db.ForeignKey('family.id'), nullable=False)

class MealSelection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    day = db.Column(db.String(10), nullable=False)
    food_choice = db.Column(db.String(100), nullable=False)

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    weekday = db.Column(db.Integer, nullable=False)
    meal_distributions = db.relationship('MealDistribution', back_populates='meal', cascade='all, delete-orphan')

class SpecialMeal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, unique=True, nullable=False)
    meal_distributions = db.relationship('MealDistribution', back_populates='special_meal', cascade='all, delete-orphan')

class MealDistribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=True)
    special_meal_id = db.Column(db.Integer, db.ForeignKey('special_meal.id'), nullable=True)
    status = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    student = db.relationship('User', back_populates='meal_distributions')
    meal = db.relationship('Meal', back_populates='meal_distributions')
    special_meal = db.relationship('SpecialMeal', back_populates='meal_distributions')

class Absence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    student = db.relationship('User', back_populates='absences')

