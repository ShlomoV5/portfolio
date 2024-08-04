from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created.")

if __name__ == "__main__":
    app.run(debug=True)