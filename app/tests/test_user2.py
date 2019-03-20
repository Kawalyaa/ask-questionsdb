import os
import json
import unittest
# import psycopg2
# from instance.config import app_config
from app.db_con import DataBaseConnection
from app import creat_app
secret = os.getenv("SECRET")
db_uri = DataBaseConnection("dbname='question_test' host='localhost' port=5432  user='kawalya' password='kawalyaa'")


class BaseTest(unittest.TestCase):
    """ The base class for seeting user tests and tearing down """

    def setUp(self):
        """ set the variables before each test """
        db_uri.drop_all_tables()
        db_uri.creat_tables()
        self.app = creat_app('testing')
        self.client = self.app.test_client()
        self.data = {
            "name": "Kawalya",
            "user_name": "andrewhi",
            "email": "andrew5@aaaa.com",
            "password": "bornagain"
        }

        self.login = {
            "user_name": "andrewhi",
            "password": "bornagain"
        }

    def tearDown(self):
        db_uri.drop_all_tables()


class UserSignUp(BaseTest):
    """ Test signup success """
    def test_user_signup(self):
        resp = self.client.post(path='/api/v2/auth/signup', data=json.dumps(self.data), headers={"content-type": "application/json"})
        self.assertEqual(resp.status_code, 201)

    def test_user_login(self):
        res = self.client.post(path='/api/v2/auth/signup', data=json.dumps(self.data), headers={"content-type": "application/json"})
        res = self.client.post(path="/api/v2/auth/login", data=json.dumps(self.login), headers={"content-type": "application/json"})
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
            "user_name": "aogoll",
            "password": "ASDASDASDAS"
        }
        res = self.client.post(path="/api/v2/auth/login", data=json.dumps(data), headers={"content-type": "application/json"})
        self.assertEqual(res.status_code, 401)
