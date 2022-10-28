import unittest
import json
from app import app
from model import api_models

url = "http://localhost:5000/users/"


class apitest_users_username(unittest.TestCase):
    def setUp(self):
        self.api_models = api_models.init_test_db() # reinitialize the database
        self.app = app.test_client()
        self.app.testing = True
        return

    def tearDown(self):
        # nothing to do here, db reinitialized when app starts
        return

    # GET method returns user details
    def test_one_user_get(self):
        # user in database
        username = 'sergkudinov'
        expected_data = {"username": "sergkudinov", "firstname": "sergei", "lastname": "kudinov"}
        response = self.app.get(url + username)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code,200)
        self.assertEqual(data, expected_data)

        # user not in database
        username = 'nobody'
        expected_data = 'User does not exist'
        response = self.app.get(url + username)
        data = response.get_data().decode('UTF-8')
        self.assertEqual(response.status_code,404)
        self.assertEqual(data, expected_data)
        return

    # DELETE method deletes the user
    def test_one_user_delete(self):
        # user successfully deleted
        username = 'lizmacca'
        expected_data = "User deleted"
        response = self.app.delete(url + username)
        data = response.get_data().decode('UTF-8')
        self.assertEqual(response.status_code,200)
        self.assertEqual(data, expected_data)

        # user not in database
        username = 'nobody'
        expected_data = 'User does not exist'
        response = self.app.delete(url + username)
        data = response.get_data().decode('UTF-8')
        self.assertEqual(response.status_code,404)
        self.assertEqual(data, expected_data)
        return

        # username is empty string
        username = ''
        expected_data = 'Username must not be empty'
        response = self.app.delete(url + username)
        data = response.get_data().decode('UTF-8')
        self.assertEqual(response.status_code,400)
        self.assertEqual(data, expected_data)
        return

    # POST method updates the user
    def test_one_user_post(self):
        # well-formed data and user exists
        user = {"username": "sergkudinov", "firstname": "sergei_the_second", "lastname": "kudinov"}
        username = 'sergkudinov'
        response = self.app.post(url + username, data=json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.get_data().decode('UTF-8'),"User updated")

        # username in url exists but does not match request body
        user = {"username": "something_else", "firstname": "elizabeth", "lastname": "mccutcheon"}
        username = 'lizmacca'
        response = self.app.post(url + username, data=json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.get_data().decode('UTF-8'),"Bad request")

        # badly-formed data (username exists)
        user = {"sergkudinov": "somejunkydata","missing":"stuff"}
        username = 'sergkudinov'
        response = self.app.post(url + username, data=json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.get_data().decode('UTF-8'),"Bad request")

        # user doesn't exist
        user = {"username": "missing_person", "firstname": "john", "lastname": "smith"}
        username = 'missing_person'
        response = self.app.post(url + username, data=json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,404)
        self.assertEqual(response.get_data().decode('UTF-8'),"User does not exist")

        # required field has empty string
        user = {"username": "sergkudinov", "firstname": "", "lastname": "kudinov"}
        username = 'sergkudinov'
        response = self.app.post(url + username, data=json.dumps(user),content_type='application/json')
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.get_data().decode('UTF-8'),"Bad request")

        return



if __name__ == "__main__":
    unittest.main()
