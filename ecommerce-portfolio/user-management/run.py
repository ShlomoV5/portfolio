from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)