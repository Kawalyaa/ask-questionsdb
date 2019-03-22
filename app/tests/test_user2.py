# import json
from app.tests.base_test import BaseTest


class UserSignUp(BaseTest):
    """ Test signup success """
    def test_user_signup(self):
        response = self.register_user("Kawalya", "andrewhi", "andrew5@aaaa.com", "bornagain")
        self.assertEqual(response.status_code, 201)

        # resp = self.client.post(path='/api/v2/auth/signup', data=json.dumps(self.data), headers={"content-type": "application/json"})
        # self.assertEqual(resp.status_code, 201)

    def test_user_login(self):
        response = self.register_user("Kawalya", "andrewhi", "andrew5@aaaa.com", "bornagain")
        response = self.login_user("andrewhi", "bornagain")
        self.assertEqual(response.status_code, 200)
        # res = self.client.post(path='/api/v2/auth/signup', data=json.dumps(self.data), headers={"content-type": "application/json"})
        # res = self.client.post(path="/api/v2/auth/login", data=json.dumps(self.login), headers={"content-type": "application/json"})
        # self.assertEqual(res.status_code, 200)

    def test_login_unexisting_user(self):
        response = self.login_user("someone", "heistheone")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['message'], "No user found")
        # data = {
        #    "user_name": "MDASD",
        #    "password": "ASDASDASDAS"
        # }
        # res = self.client.post(path="/api/v2/auth/login", data=json.dumps(data), headers={"content-type": "application/json"})
        # self.assertEqual(res.status_code, 401)
        # self.assertEqual(res.json['message'], "No user found")

    def test_unmatching_creds(self):
        response = self.login_user("andrewhi", "ccccccc")
        self.assertEqual(response.status_code, 401)
        # data = {
        #    "user_name": "aogoll",
        #    "password": "ASDASDASDAS"
        # }
        # res = self.client.post(path="/api/v2/auth/login", data=json.dumps(data), headers={"content-type": "application/json"})
        # self.assertEqual(res.status_code, 401)
