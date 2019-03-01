import json
import unittest
from app import creat_app
from app.db_config2 import destroydb, init_tdb


class TestUser(unittest.TestCase):
    def setUp(self):
        destroydb()
        self.app = creat_app('testing')
        self.client = self.app.test_client()
        self.user = {
            "name": "Andrew",
            "user_name": "andrew5",
            "password": "bornagain",
            "email": "andrew5@gmail.com"
        }

        # self.error_msg = "The path accessed / resource requested cannot be found, please check"
        destroydb()
        with self.app.app_context():
            self.db = init_tdb()

    def test_user_registration(self):
        res = self.client.post('/api/v2/auth/signup', data=json.dumps(self.user), headers={"content-type": "application/json"})
        self.assertEqual(res.status_code, 201)

    def test_user_login(self):
        self.client.post('/api/v2/auth/signup', data=json.dumps(self.user), headers={"content-type": "application/json"})
        payload = {
            "user_name": "andrew5",
            "password": "bornagain"
        }

        login = self.client.post('api/v2/auth/login', data=payload)
        self.assertEqual(login.status_code, 200)

    def test_login_unexisting_user(self):
        new_user = {
            "user_name": "nicebug",
            "password": "filper44h"
        }

        res = self.client.post("/api/v2/auth/login", data=json.dumps(new_user), headers={"content-type": "application/json"})
        self.assertEqual(res.status_code, 401)
        self.assertEqual(res.json["message"], "No user found")

    def test_unmatching_cred(self):
        un_match = {
            "user_name": "andrew5",
            "password": "inimformed"
        }

        res = self.client.post("/api/v2/auth/login", data=json.dumps(un_match), headers={"content-type": "application/json"})
        self.assertEqual(res.status_code, 401)
        self.assertEqual(res.json["message"], "No user found")

    def tearDown(self):
        with self.app.app_context():
            destroydb()
            self.db.commit()
            self.db.close()


if __name__ == '__main__':
    unittest.main()
