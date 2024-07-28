import unittest
from app import create_app, db
from app.models import Usuario, Producto, Ingrediente, Base, Complemento

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            self.populate_db()

    def populate_db(self):
        usuario = Usuario(username='testuser', password='testpass', es_admin=True)
        db.session.add(usuario)
        db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_login(self):
        response = self.client.post('/login', data=dict(username='testuser', password='testpass'))
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
