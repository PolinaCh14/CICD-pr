import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_products(self):
        response = self.app.get('/api/products')
        self.assertEqual(response.status_code, 200)

    def test_post_product(self):
        response = self.app.post('/api/products', json={
            'name': 'Test Product',
            'price': 10.0
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
