import unittest
import json
from model import api_models
from services import api_services

class unittest_getuser(unittest.TestCase):
    def setUp(self):
        self.api_models = api_models.init_test_db() # reinitialize the database
        return

    def tearDown(self):
        # nothing to do here, db reinitialized when app starts
        return

    def test_get_user(self):
        # user exists
        username = 'sergkudinov'
        data = api_services.get_user(username)
        expected_data = '{"username": "sergkudinov", "firstname": "sergei", "lastname": "kudinov"}'
        self.assertEqual(data,expected_data)

        # user doesn't exists
        username = 'mysteryman'
        data = data = api_services.get_user(username)
        expected_data = None
        self.assertEqual(data,expected_data)
        return
