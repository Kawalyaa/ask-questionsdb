
import json
import unittest

from app import creat_app
from app.db_con import destroydb, init_tdb


class TestUser(unittest.TestCase):
    """docstring for TestUser"""

    def setUp(self):
        destroydb()
        init_tdb()
        self.app = creat_app('testing')
        self.client = self.app.test_client()
        # everytime you run the test you must change the user_name coz signup is once
        self.data = {
            "name": "Andrew",
            "user_name": "devlandrew5",
            "password": "bornagain",
            "email": "andrew5@gmail.com"
        }
        self.dataa = {
            "user_name": "andrew5",
            "password": "bornagain"
        }

    def tearDown(self):
        destroydb()

    def test_user_registration(self):
        resp = self.client.post(path="/api/v2/auth/signup", data=json.dumps(self.data), headers={"content-type": "application/json"})
        self.assertEqual(resp.status_code, 201)

    def test_user_login(self):
        res = self.client.post(path="/api/v2/auth/login", data=json.dumps(self.dataa), headers={"content-type": "application/json"})
        self.assertEqual(res.status_code, 200)

    def test_login_unexisting_user(self):
        data = {
            "user_name": "MDASD",
            "password": "ASDASDASDAS"
        }
        res = self.client.post(path="/api/v2/auth/login", data=json.dumps(data), headers={"content-type": "application/json"})
        self.assertEqual(res.status_code, 401)
        self.assertEqual(res.json['message'], "No user found")

    def test_unmatching_creds(self):

        data = {
            "user_name": "andrew5",
            "password": "ASDASDASDAS"
        }
        res = self.client.post(path="/api/v2/auth/login", data=json.dumps(data), headers={"content-type": "application/json"})
        self.assertEqual(res.status_code, 401)
