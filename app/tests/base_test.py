# import os
import json
import unittest
from app.db_con import DataBaseConnection
from app import creat_app
# secret = os.getenv("SECRET")
db_uri = DataBaseConnection("dbname='question_test' host='localhost' port=5432  user='kawalya' password='kawalyaa'")


class BaseTest(unittest.TestCase):
    """ The base class for seeting user tests and tearing down """

    def setUp(self):
        """ set the variables before each test """
        # db_uri.drop_all_tables()
        db_uri.creat_tables()
        self.app = creat_app('testing')
        self.client = self.app.test_client()
        # self.data = {
        #    "name": "Kawalya",
        #    "email": "andrew5@aaaa.com",
        #    "password": "bornagain"
        # }

        # self.login = {
        #    "user_name": "andrewhi",
        #    "password": "bornagain"
        # }

        self.data2 = {
            "title": "WORLDI NEWZ",
            "description": "Is CCTV found in central china!!",
            "created_by": 1
        }

    def tearDown(self):
        db_uri.drop_all_tables()

    # def post_question_by_user(self):  # This is the method that made post test pass
    #    """create a fictitious user"""
    #    response = self.register_user("Kawalya", "andrewhi", "andrew5@aaaa.com", "bornagain")
    #    response = self.login_user("andrewhi", "bornagain")
    #    token = response.json['access_token']
    #    # res = 'Authorization: Bearer {}'.format(access_token)
    #    res = self.client.post('api/v2/question', data=json.dumps(self.data2), content_type='application/json', headers={"Authorization": "Bearer {}".format(token)})
    #    return res

    # def get_all_question_by_user(self):  # This is the method that made post test pass
    #    response = self.register_user("Kawalya", "andrewhi", "andrew5@aaaa.com", "bornagain")
    #    response = self.login_user("andrewhi", "bornagain")
    #    token = response.json['access_token']
    #    # res = 'Authorization: Bearer {}'.format(access_token)
    #    # res = self.client.post('api/v2/question', data=json.dumps(self.data2), content_type='application/json', headers={"Authorization": "Bearer {}".format(token)})
    #    res = self.client.get('api/v2/question', content_type='application/json', headers={"Authorization": "Bearer {}".format(token)})
    #    return res

    # def post_data(self, path='/api/v2/question', data={}):
    #    """This function performs a POST request using the testing client"""
    #    if not data:
    #        data = self.data2
    #    auth_token = self.create_user()
    #    headers = {"Authorization": "Bearer {}".format(auth_token)}
    #    result = self.client.post(path, data=json.dumps(data),
    #                              headers=headers,
    #                              content_type='application/json')
    #    return result

    def login_user(self, user_name, password):
        """
        Method for logging a user with dummy data
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

    def post_aquestion_route(self, token):  # This is the method that made post test pass
        """create a fictitious user"""
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
    # def post_question(self, token, title, description, created_by):
    #    """
    #    Method for posting a question
    #    """
    #    return self.client.post(
    #        'api/v2/question',
    #        data=json.dumps(dict(
    #            title=title,
    #            description=description,
    #            created_by=created_by
    #        )
    #        ),
    #        content_type='application/json',
    #        headers={'Authorization': 'Bearer {}'.format(token)}
    #    )

    # def register_user2(self, path="/api/v2/auth/signup", data={}):
        # db_uri.drop_all_tables()
    #    if not data:
    #        data = {
    #            "name": "Kawalya",
    #            "user_name": "andrewhi",
    #            "email": "andrew5@aaaa.com",
    #            "password": "bornagain"
    #        }
    #    header = {"content-type": "application/json"}
    #    res = self.client.post(path=path, data=json.dumps(data), headers=header)
    #    return res.json['access_token']

    # def post(self, path="/api/v2/question", data={}):
    #    if not data:
    #        data = self.data
    #    token = self.register_user()
    #    header = {
    #        "Authorization": "Bearer {}".format(token),
    #        "content-type": "application/json"
    #    }
    #    res = self.client.post(path=path, data=json.dumps(data), headers=header)
    #    return res

    # def post(self, path="/api/v2/question", data={}):
    #    if not data:
    #        data = self.data
    #    token = self.register_user2()
    #    header = {
    #        "Authorization": "Bearer {}".format(token),
    #        "content-type": "application/json"
    #    }
    #    res = self.client.post(path=path, headers=header)
    #    return res

    def get_token(self):
        """Returns user token"""
        response = self.register_user("Kawalya", "andrewhi", "andrew5@aaaa.com", "bornagain")
        response = self.login_user("andrewhi", "bornagain")
        token = response.json['access_token']
        return token
