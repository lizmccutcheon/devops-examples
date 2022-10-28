import unittest
import json
from model import api_models
from services import api_services


class unittest_updateusers(unittest.TestCase):
    def setUp(self):
        self.api_models = api_models.init_test_db() # reinitialize the database
        return

    def tearDown(self):
        # nothing to do here, db reinitialized when app starts
        return

    def test_update_users(self):
        # username doesn't exist
        username = 'nobody'
        firstname = 'asdf'
        lastname = 'asdf'
        data_before = api_services.get_users()
        expected_data_after = '{"Users": [{"username": "sergkudinov", "firstname": "sergei", "lastname": "kudinov"}, {"username": "lizmacca", "firstname": "elizabeth", "lastname": "mccutcheon"}]}'
        api_services.update_user(username,firstname,lastname)
        data_after = api_services.get_users()
        self.assertEqual(data_after,expected_data_after)

        # username exists
        username = 'lizmacca'
        firstname = 'new_liz'
        lastname = 'new_mccutcheon'
        data_before = api_services.get_users()
        expected_data_after = '{"Users": [{"username": "sergkudinov", "firstname": "sergei", "lastname": "kudinov"}, {"username": "lizmacca", "firstname": "new_liz", "lastname": "new_mccutcheon"}]}'
        api_services.update_user(username,firstname,lastname)
        data_after = api_services.get_users()
        self.assertEqual(data_after,expected_data_after)

        # username missing
        username = ''
        firstname = 'asdf'
        lastname = 'asdf'
        expected_data_after = api_services.get_users()
        api_services.update_user(username,firstname,lastname)
        data_after = api_services.get_users()
        self.assertEqual(data_after,expected_data_after)

        # other data missing
        username = 'sergkudinov'
        firstname = ''
        lastname = ''
        expected_data_after = api_services.get_users()
        api_services.update_user(username,firstname,lastname)
        data_after = api_services.get_users()
        self.assertEqual(data_after,expected_data_after)

        return
