from flask_sqlalchemy import SQLAlchemy
from datetime import date
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    students = db.relationship('Student', back_populates='family', cascade='all, delete-orphan')
    tokens = db.relationship('Token', back_populates='user', cascade='all, delete-orphan')

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='tokens')

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    class_name = db.Column(db.String(100), nullable=False)
    family_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    family = db.relationship('User', back_populates='students')

class Absence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    student = db.relationship('Student')

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255))

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weekday = db.Column(db.String(10), nullable=False)  # "Monday", "Tuesday", etc.
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=False)
    is_default = db.Column(db.Boolean, default=False)
    meal = db.relationship('Meal')

class SpecialMeal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=False)
    meal = db.relationship('Meal')

class MealGiveout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    student = db.relationship('Student')
