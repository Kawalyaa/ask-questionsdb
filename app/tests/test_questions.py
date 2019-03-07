import json
import unittest

from app import creat_app
from app.db_con import destroydb, init_tdb


class TestUser(unittest.TestCase):
    """docstring for TestUser"""

    def setUp(self):
        self.app = creat_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            self.db = init_tdb()
        self.data = {
            "title": "Test  3 ",
            "description": "Lorem ",
            "created_by": 4
        }

    def register_user(self, path="/api/v2/auth/signup", data={}):
        destroydb()
        if not data:
            data = {
                "name": "Andrew",
                "user_name": "devperandrew5",
                "password": "bornagain",
                "email": "andrew5@gmail.com"
            }
        header = {"content-type": "application/json"}
        res = self.client.post(path=path, data=json.dumps(data), headers=header)
        return res.json['access_token']

    def post(self, path="/api/v2//question", data={}):
        if not data:
            data = self.data
        token = self.register_user()
        header = {
            "Authorization": "Bearer {}".format(token),
            "content-type": "application/json"
        }
        res = self.client.post(path=path, data=json.dumps(data), headers=header)
        return res

    def get(self, path="/api/v2//question", data={}):
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
