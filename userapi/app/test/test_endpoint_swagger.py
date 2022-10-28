import unittest
import json
from app import app
from model import api_models
from flask import Flask
from flask import render_template

url = "http://localhost:5000/swagger/"

class apittest_index(unittest.TestCase):
    def setUp(self):
        self.api_models = api_models.init_test_db() # reinitialize the database
        self.app = app.test_client()
        self.app.testing = True
        return

    def tearDown(self):
        # nothing to do here
        return

    # GET swagger page
    def test_swagger_get(self):
        response = self.app.get(url)
        html = response.data.decode()
        self.assertEqual(response.status_code,200)
        self.assertTrue('My Stupid Flask API' in html)
        return

    # POST not allowed
    def test_swagger_post(self):
        response = self.app.post(url)
        self.assertEqual(response.status_code,405)
        return

    # DELETE not allowed
    def test_swagger_delete(self):
        response = self.app.delete(url)
        self.assertEqual(response.status_code,405)
        return


if __name__ == "__main__":
    unittest.main()
