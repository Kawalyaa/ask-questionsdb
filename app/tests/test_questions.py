from app.tests.base_test import BaseTest


class TestPosts(BaseTest):
    """docstring for TestUser"""

    def test_posting_blog(self):
        res = self.post_question_by_user()
        self.assertTrue(res.status_code, 201)
        self.assertTrue(res.json['message'], "created")
        # new_question = self.post_data()
        # response = self.register_user("Kawalya", "andrewhi", "andrew5@aaaa.com", "bornagain")
        # response = self.login_user("andrewhi", "bornagain")
        # token = response.json['access_token']
        # res = self.post_question(token, "WORLDI NEWZ", "Is CCTV found in central china!!", 1)

    def test_getting_blog(self):
        res = self.get()
        self.assertEqual(res.status_code, 200)
# with self.client:
#    response = self.register_user("Kawalya", "andrewhi", "andrew5@aaaa.com", "bornagain")
#    response = self.login_user("andrewhi", "bornagain")
#    # token = self.get_token()
#    response = self.post_question("INFOMATION", "Is CCTV found in central china!!", 4
