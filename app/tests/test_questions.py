from app.tests.base_test import BaseTest


class TestPosts(BaseTest):
    """docstring for TestUser"""

    def test_posting_blog(self):
        res = self.post()
        self.assertEqual(res.status_code, 201)

    def test_getting_blog(self):
        res = self.get()
        self.assertEqual(res.status_code, 200)
# with self.client:
#    response = self.register_user("Kawalya", "andrewhi", "andrew5@aaaa.com", "bornagain")
#    response = self.login_user("andrewhi", "bornagain")
#    # token = self.get_token()
#    response = self.post_question("INFOMATION", "Is CCTV found in central china!!", 4
