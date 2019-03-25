from app.tests.base_test import BaseTest


class TestPosts(BaseTest):
    """docstring for TestUser"""

    def test_posting_blog(self):
        # res = self.post_question_by_user()
        res = self.posting_question()
        self.assertTrue(res.status_code, 201)
        self.assertTrue(res.json['message'], "created")

    def test_getting_blog(self):
        res = self.get_qtn()
        self.assertTrue(res.status_code, 200)
        self.assertTrue(res.json['message'], "ok")

    def test_getting_one_qtn(self):
        res = self.get_asingle_qtn()
        self.assertTrue(res.status_code, 200)
        self.assertTrue(res.json['message'], "ok")

    def test_editing_qtn(self):
        res = self.edit_aqtn()
        self.assertTrue(res.status_code, 200)
        self.assertTrue(res.json['message'], "question with id 1 is updated")

    def test_deleting_aqtn(self):
        res = self.delete_aqtn()
        self.assertTrue(res.status_code, 200)
        self.assertTrue(res.json['message'], "question with id 1 is Deleted")

    def test_post_with_no_token(self):
        res = self.post_with_no_token()
        self.assertTrue(res.status_code, 403)
        self.assertTrue(res.json['message'], "No authorization header provided. This resource is secured")

    def test_getting_from_empty_database(self):
        res = self.get_from_empty_database()
        self.assertTrue(res.json['message'], "Database is empty")
