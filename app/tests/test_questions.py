from app.tests.base_test import BaseTest


class TestPosts(BaseTest):
    """docstring for TestUser"""

    def test_posting_blog(self):
        # res = self.post_question_by_user()
        res = self.posting_question()
        self.assertTrue(res.status_code, 201)
        self.assertTrue(res.json['message'], "created")

    def test_getting_blog(self):
        response = self.get_qtn()
        self.assertTrue(response.status_code, 200)

        # res = self.get_all_question_by_user()
        # self.assertEqual(res.status_code, 200)
        # with self.client:
        #    response = self.register_user("Kawalya", "andrewhi", "andrew5@aaaa.com", "bornagain")
        #    response = self.login_user("andrewhi", "bornagain")
        #    # token = self.get_token()
        #    response = self.post_question("INFOMATION", "Is CCTV found in central china!!"
