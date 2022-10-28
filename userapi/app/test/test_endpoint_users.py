import unittest
import json
from app import app
from model import api_models

url = "http://localhost:5000/users"


class apitest_users(unittest.TestCase):
    def setUp(self):
        self.api_models = api_models.init_test_db() # reinitialize the database
        self.app = app.test_client()
        self.app.testing = True
        return

    def tearDown(self):
        # nothing to do here, db reinitialized when app starts
        return

    # GET method returns all users
    def test_all_users_get(self):
        response = self.app.get(url)
        data = json.loads(response.get_data())
        expected_data = {"Users":[{"username": "sergkudinov", "firstname": "sergei", "lastname": "kudinov"},{"username": "lizmacca", "firstname": "elizabeth", "lastname": "mccutcheon"}]}
        self.assertEqual(response.status_code,200)
        self.assertEqual(data,expected_data)

    # POST method creates a new user
    def test_all_users_post(self):
        # well-formed data and user doesn't already exist
        user = {"username": "new_username", "firstname": "new_firstname", "lastname": "new_lastname"}
        response = self.app.post(url, data=json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,201)

        # bady-formed data
        user = {"usere": "somejunkydata","missing":"stuff"}
        response = self.app.post(url, data=json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.get_data().decode('UTF-8'),"Bad request")

        # required field has empty string
        user = {"username": "another_new_username", "firstname": "", "lastname": "newlastname"}
        response = self.app.post(url, data=json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.get_data().decode('UTF-8'),"Bad request")

        # user already exists
        user = {"username": "sergkudinov", "firstname": "sergei", "lastname": "kudinov"}
        response = self.app.post(url, data=json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,409)
        self.assertEqual(response.get_data().decode('UTF-8'),"User already exists")

        return

    # DELETE method not allowed
    def test_all_users_delete(self):
        response = self.app.delete(url)
        self.assertEqual(response.status_code,405)


if __name__ == "__main__":
    unittest.main()
