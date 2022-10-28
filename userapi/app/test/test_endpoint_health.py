import unittest
import json
from app import app
from model import api_models

url = 'http://localhost:5000/health'

class apitest_health(unittest.TestCase):
    def setUp(self):
        self.api_models = api_models.init_test_db() # reinitialize the database
        self.app = app.test_client()
        self.app.testing = True
        return

    def tearDown(self):
        # nothing to do here
        return

    # GET
    def test_health_get(self):
        response = self.app.get()
        self.assertEqual(response.status_code,200)
        return

    # POST method not allowed
    def test_health_post(self):
        response = self.app.post(url)
        self.assertEqual(response.status_code,405)
        return

    # DELETE method not allowed
    def test_health_delete(self):
        response = self.app.delete(url)
        self.assertEqual(response.status_code,405)
        return


if __name__ == "__main__":
    unittest.main()
