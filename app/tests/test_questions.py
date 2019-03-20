import json
import unittest
# from app.db_con import DataBaseConnection
from app.tests.test_user2 import BaseTest
from app import creat_app
# db_uri = DataBaseConnection("dbname='question_test' host='localhost' port=5432  user='kawalya' password='kawalyaa'")


class TestUser(unittest.TestCase):
    """docstring for TestUser"""

    def setUp(self):
        # db_uri.drop_all_tables()
        # db_uri.creat_tables()
        self.app = creat_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            self.db = db_uri.creat_tables()
        self.data = {
            "title": "WORLDI NEWZ",
            "description": "Is CCTV found in central china!!",
            "created_by": 4
        }

    def register_user(self, path="/api/v2/auth/signup", data={}):
        db_uri.drop_all_tables()
        if not data:
            data = {
                "name": "Kawalya",
                "user_name": "andrewhi",
                "email": "andrew5@aaaa.com",
                "password": "bornagain"
            }
            login = {
                "user_name": "andrewhi",
                "password": "bornagain"
            }
        header = {"content-type": "application/json"}
        res = self.client.post(path=path, data=json.dumps(data), headers=header)
        res = self.client.post(path="/api/v2/auth/login", data=json.dumps(login), headers={"content-type": "application/json"})
        return res.json['access_token']

    def post(self, path="/api/v2/question", data={}):
        if not data:
            data = self.data
        token = self.register_user()
        header = {
            "Authorization": "Bearer {}".format(token),
            "content-type": "application/json"
        }
        res = self.client.post(path=path, data=json.dumps(data), headers=header)
        return res

    def get(self, path="/api/v2/question", data={}):
        token = self.register_user()
        header = {
            "Authorization": "Bearer {}".format(token),
            "content-type": "application/json"
        }
        res = self.client.get(path=path, headers=header)
        return res

    def test_posting_blog(self):
        res = self.post()
        self.assertEqual(res.status_code, 201)

    def test_getting_blog(self):
        res = self.get()
        self.assertEqual(res.status_code, 200)
