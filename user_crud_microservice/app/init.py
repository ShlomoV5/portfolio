from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:password@host:port/database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   


db = SQLAlchemy(app)

from app import routes, models