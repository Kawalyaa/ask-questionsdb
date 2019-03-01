
import json
import unittest

from app import creat_app
from app.db_config import destroydb, init_tdb


class TestUser(unittest.TestCase):
    """docstring for TestUser"""

    def setUp(self):
        destroydb()
        init_tdb()
        self.app = creat_app('testing')
        self.client = self.app.test_client()
        # with self.app.app_context():
        #    self.db = init_tdb()
        self.data = {
            "name": "AbrahamOgol",
            "user_name": "aogoll",
            "email": "a5@aaaa.com",
            "password": "mcogols"
        }

    def tearDown(self):
        init_tdb()

    # def register(self, path="/api/v2/auth/signup", data):
    #    destroydb()
    #    if not data:
    #        data = self.data
    #    res = self.client.post(path=path, data=json.dumps(data), headers={"content-type": "application/json"})
    #    return res

    def test_user_registration(self):
        resp = self.client.post(path='/api/v2/auth/signup', data=json.dumps(self.data), headers={"content-type": "application/json"})
        self.assertEqual(resp.status_code, 201)

    def test_user_login(self):
        # regis = self.register()
        res = self.client.post(path="/api/v2/auth/login", data=json.dumps(self.data), headers={"content-type": "application/json"})
        self.assertEqual(res.status_code, 401)

    def test_login_unexisting_user(self):
        data = {
            "user_name": "MDASD",
            "password": "ASDASDASDAS"
        }
        res = self.client.post(path="/api/v2/auth/login", data=json.dumps(data), headers={"content-type": "application/json"})
        self.assertEqual(res.status_code, 401)
        self.assertEqual(res.json['message'], "No user found")

    def test_unmatching_creds(self):
        # regis = self.register()
        data = {
            "user_name": "aogoll",
            "password": "ASDASDASDAS"
        }
        res = self.client.post(path="/api/v2/auth/login", data=json.dumps(data), headers={"content-type": "application/json"})
        self.assertEqual(res.status_code, 401)
        # self.assertEqual(res.json['message'], "Username and password does not macth")

    # def teaDown(self):
    #    with self.app.app_context():
    #        destroydb()
    #        self.db.commit()
    #        self.db.close()
