import unittest
import json
from model import api_models
from services import api_services


class unittest_getusers(unittest.TestCase):
    def setUp(self):
        self.api_models = api_models.init_test_db() # reinitialize the database
        return

    def tearDown(self):
        # nothing to do here, db reinitialized when app starts
        return

    def test_get_users(self):
        data = api_services.get_users()
        expected_data = '{"Users": [{"username": "sergkudinov", "firstname": "sergei", "lastname": "kudinov"}, {"username": "lizmacca", "firstname": "elizabeth", "lastname": "mccutcheon"}]}'
        self.assertEqual(data,expected_data)
        return
