import json
import unittest

from app import creat_app
# from app.db_con import destroydb, init_tdb


class TestUser(unittest.TestCase):
    """docstring for TestUser"""
    def create_user(self):
        """create a fictitious user"""
        # username = "".join(choice(
        #                   string.ascii_letters) for x in range(randint(7, 10)))
        data = {
            "name": "Andrew",
            "user_name": "devperandrew5",
            "password": "bornagain",
            "email": "andrew5@gmail.com"
        }
        path = "/api/v2/auth/signup"
        user = self.client.post(path,
                                data=json.dumps(data),
                                content_type="application/json")

        # user_id = user.json['user_id']
        auth_token = user.json['access_token']
        return auth_token

    def setUp(self):
        self.app = creat_app('testing')
        self.client = self.app.test_client()

        self.question = {
            "title": "Test  3 ",
            "description": "Lorem ",
            "created_by": 4
        }

    def post_data(self, path='/api/v2/question', auth_token=2, data={}, headers=0):
        """This function performs a POST request using the testing client"""
        if not data:
            data = self.question
        if auth_token is 2:
            user = self.create_user()
            auth_token = user[1]
        if not headers:
            headers = {"Authorization": "Bearer {}".format(auth_token)}
        result = self.client.post(path, data=json.dumps(data),
                                  headers=headers,
                                  content_type='application/json')
        return result

    # def register_user(self, path="/api/v2/auth/signup", data={}):
    #    if not data:
    #        data = {
    #            "name": "Andrew",
    #            "user_name": "devperandrew5",
    #            "password": "bornagain",
    #            "email": "andrew5@gmail.com"
    #        }
    #    header = {"content-type": "application/json"}
    #    res = self.client.post(path=path, data=json.dumps(data), headers=header)
    #    return res["access_token"]

    # def post(self, path="/api/v2//question", data={}):
    #    if not data:
    #    token = self.register_user()
    #    header = {
    #        "Authorization": "Bearer {}".format(token),
    #        "content-type": "application/json"
    #    }
    #    res = self.client.post(path=path, data=json.dumps(data), headers=header)
    #    return res
    def get_data(self, path='/api/v2/question'):
        """This function performs a GET request to a given path
            using the testing client
        """
        result = self.client.get(path)
        return result

    # def get(self, path="/api/v2//question", data={}):
    #    token = self.register_user()
    #    header = {
    #        "Authorization": "Bearer {}".format(token),
    #        "content-type": "application/json"
    #    }
    #    res = self.client.get(path=path, headers=header)
    #    return res

    def test_post_question(self):
        """Test that a user can post a question
        """
        new_question = self.post_data()
        # test that the server responds with the correct status code
        self.assertEqual(new_question.status_code, 201)
        # self.assertTrue(new_question.json['message'])
        # self.assertTrue(new_question.json['question_id'])

    # def test_posting_blog(self):
    #    res = self.post()
    #    self.assertEqual(res.status_code, 201)

    def test_get_questions(self):
        """Test that the api can respond with a list of questions"""
        new_question = self.post_data()
        questions = self.get_data().json
        self.assertEqual(questions.status_code, 200)
        # self.assertEqual(questions['message'], 'success')
        # self.assertIn(new_question.json['text'], str(questions['questions']))

    def test_getting_blog(self):
        res = self.get()
        self.assertEqual(res.status_code, 200)
