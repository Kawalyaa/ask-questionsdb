# import os
import json
import unittest
from app import creat_app


class BaseTest(unittest.TestCase):
    """ The base class for seting user tests and tearing down """

    def setUp(self):
        """ set the variables before each test """
        self.app = creat_app('testing')
        self.client = self.app.test_client()

        self.data2 = {
            "title": "WORLDI NEWZ",
            "description": "Is CCTV found in central china!!",
            "created_by": 1
        }

    def tearDown(self):
        # db_uri.drop_all_tables()
        pass

    def login_user(self, user_name, password):
        """
        Method for logging a user
        """
        return self.client.post(
            '/api/v2/auth/login',
            data=json.dumps({
                "user_name": user_name,
                "password": password}
            ),
            content_type='application/json'
        )

    def register_user(self, name, user_name, email, password):
        """
        Method for registering a user
        """
        return self.client.post(
            '/api/v2/auth/signup',
            data=json.dumps(dict(
                name=name,
                user_name=user_name,
                email=email,
                password=password
            )
            ),
            content_type='application/json'
        )

    def logout_user(self, path='/api/v2/auth/logout'):
        """Thid method logs out user"""
        token = self.get_token()
        header = {
            "Authorization": "Bearer {}".format(token),
            "content_type": "application/json"
        }
        res = self.client.post(path=path, headers=header)
        return res

    def post_aquestion_route(self, token):
        """This method takes in token to generate post question route"""
        res = self.client.post('api/v2/question', data=json.dumps(self.data2), content_type='application/json', headers={"Authorization": "Bearer {}".format(token)})
        return res

    def get_qtn(self, path="/api/v2/question"):
        token = self.get_token()
        self.post_aquestion_route(token)

        header = {
            "Authorization": "Bearer {}".format(token),
            "content-type": "application/json"
        }
        res = self.client.get(path=path, headers=header)
        return res

    def posting_question(self):
        token = self.get_token()
        res = self.post_aquestion_route(token)
        return res

    def get_asingle_qtn(self, path="/api/v2/question/1"):
        token = self.get_token()
        self.post_aquestion_route(token)
        header = {
            "Authorization": "Bearer {}".format(token),
            "content-type": "application/json"
        }
        res = self.client.get(path=path, headers=header)
        return res

    def edit_aqtn(self, path="/api/v2/question/1"):
        token = self.get_token()
        self.post_aquestion_route(token)
        header = {
            "Authorization": "Bearer {}".format(token),
            "content_type": "application/json"
        }
        res = self.client.put(path=path, headers=header)
        return res

    def delete_aqtn(self, path="/api/v2/question/1"):
        token = self.get_token()
        self.post_aquestion_route(token)
        header = {
            "Authorization": "Bearer {}".format(token),
            "content_type": "application/json"
        }
        res = self.client.delete(path=path, headers=header)
        return res

    def post_with_no_token(self):
        """posting question witth no token"""
        res = self.client.post('api/v2/question', data=json.dumps(self.data2), content_type='application/json', headers={"Authorization": "Bearer {}"})
        return res

    def get_from_empty_database(self, path="/api/v2/question"):
        token = self.get_token()
        header = {
            "Authorization": "Bearer {}".format(token),
            "content-type": "application/json"
        }
        res = self.client.get(path=path, headers=header)
        return res

    def get_token(self):
        """Returns user token"""
        response = self.register_user("Kawalya", "andrewhi", "andrew5@aaaa.com", "bornagain")
        response = self.login_user("andrewhi", "bornagain")
        token = response.json['access_token']
        return token
