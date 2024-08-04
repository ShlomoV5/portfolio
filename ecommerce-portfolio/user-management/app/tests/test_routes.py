import unittest
from app import create_app, db
from app.models import User

class UserRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user(self):
        response = self.client.post('/users', json={'username': 'testuser', 'email': 'test@example.com', 'password': 'password'})
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        self.client.post('/users', json={'username': 'testuser', 'email': 'test@example.com', 'password': 'password'})
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn('testuser', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
