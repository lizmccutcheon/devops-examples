import unittest
import json
from app import app
from model import api_models

url = 'http://localhost:5000/hello'

class db_test(unittest.TestCase):
    def setUp(self):
        self.api_models = api_models.init_test_db() # reinitialize the database
        self.app = app.test_client()
        self.app.testing = True
        return

    def tearDown(self):
        # nothing to do here
        return

    # check db connection works
    def test_db_connection(self):
        conn = api_models.get_connection()
        expected_val = True
        try:
            conn.cursor()
            val = True
        except:
            val = False
        self.assertEqual(val,expected_val)
        return

    # check database schema
    def test_check_schema(self):
        # check table exists
        conn = api_models.get_connection()
        expected_result = 'users'
        rows = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchone()
        conn.close()
        result = rows['name']
        self.assertEqual(expected_result,result)

        # check schema is correct
        conn = api_models.get_connection()
        rows = conn.execute("PRAGMA table_info('users')").fetchall()
        conn.close()
        expected_row1 = [0, 'username', 'VARCHAR(40)', 0, None, 1]
        expected_row2 = [1, 'firstname', 'VARCHAR(20)', 1, None, 0]
        expected_row3 = [2, 'lastname', 'VARCHAR(20)', 1, None, 0]
        row1 = [rows[0][0],rows[0][1],rows[0][2],rows[0][3],rows[0][4],rows[0][5]]
        row2 = [rows[1][0],rows[1][1],rows[1][2],rows[1][3],rows[1][4],rows[1][5]]
        row3 = [rows[2][0],rows[2][1],rows[2][2],rows[2][3],rows[2][4],rows[2][5]]
        self.assertEqual(row1, expected_row1)
        self.assertEqual(row2, expected_row2)
        self.assertEqual(row3, expected_row3)
        return


if __name__ == "__main__":
    unittest.main()
