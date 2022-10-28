import unittest
import json
from app import app
from model import api_models
from services import api_services

class unittest_adduser(unittest.TestCase):

    def setUp(self):
        self.api_models = api_models.init_test_db() # reinitialize the database
        self.app = app.test_client()
        self.app.testing = True
        return

    def tearDown(self):
        return

    def test_add_user(self):
        # user already exists
        username = 'lizmacca'
        firstname = 'elizabeth'
        lastname = 'mccutcheon'
        data_before = api_services.get_users()
        expected_data_after = data_before
        api_services.add_user(username,firstname,lastname)
        data_after = api_services.get_users()
        self.assertEqual(expected_data_after, data_after)

        # user doesn't exist yet
        username = 'lizmacca2'
        firstname = 'elizabeth'
        lastname = 'mccutcheon'
        data_before = api_services.get_users()
        expected_data_after = '{"Users": [{"username": "sergkudinov", "firstname": "sergei", "lastname": "kudinov"}, {"username": "lizmacca", "firstname": "elizabeth", "lastname": "mccutcheon"}, {"username": "lizmacca2", "firstname": "elizabeth", "lastname": "mccutcheon"}]}'
        api_services.add_user(username,firstname,lastname)
        data_after = api_services.get_users()
        self.assertEqual(expected_data_after, data_after)


if __name__ == "__main__":
    unittest.main()
