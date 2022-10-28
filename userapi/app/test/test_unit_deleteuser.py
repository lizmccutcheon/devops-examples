import unittest
import json
from model import api_models
from services import api_services

class unittest_deleteuser(unittest.TestCase):
    def setUp(self):
        self.api_models = api_models.init_test_db() # reinitialize the database
        return

    def tearDown(self):
        # nothing to do here, db reinitialized when app starts
        return

    def test_delete_user(self):
        # user doesn't exist
        username = 'mysteryman'
        expected_data_before = '{"Users": [{"username": "sergkudinov", "firstname": "sergei", "lastname": "kudinov"}, {"username": "lizmacca", "firstname": "elizabeth", "lastname": "mccutcheon"}]}'
        expected_data_after = '{"Users": [{"username": "sergkudinov", "firstname": "sergei", "lastname": "kudinov"}, {"username": "lizmacca", "firstname": "elizabeth", "lastname": "mccutcheon"}]}'
        data_before = api_services.get_users()
        api_services.delete_user(username)
        data_after = api_services.get_users()
        self.assertEqual(data_before,expected_data_before)
        self.assertEqual(data_after,expected_data_after)

        # user exists
        username = 'sergkudinov'
        expected_data_before = '{"Users": [{"username": "sergkudinov", "firstname": "sergei", "lastname": "kudinov"}, {"username": "lizmacca", "firstname": "elizabeth", "lastname": "mccutcheon"}]}'
        expected_data_after = '{"Users": [{"username": "lizmacca", "firstname": "elizabeth", "lastname": "mccutcheon"}]}'
        data_before = api_services.get_users()
        api_services.delete_user(username)
        data_after = api_services.get_users()
        self.assertEqual(data_before,expected_data_before)
        self.assertEqual(data_after,expected_data_after)

        return
