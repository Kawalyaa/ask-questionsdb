from app.tests.base_test import BaseTest


class UserSignUp(BaseTest):
    """ Test signup success """
    def test_user_signup(self):
        response = self.register_user("Kawalya", "andrewhi", "andrew5@aaaa.com", "bornagain")
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        response = self.register_user("Kawalya", "andrewhi", "andrew5@aaaa.com", "bornagain")
        response = self.login_user("andrewhi", "bornagain")
        self.assertEqual(response.status_code, 200)

    def test_logout_user(self):
        """Testing logout user"""
        res = self.logout_user()
        self.assertTrue(res.status_code, 200)
        self.assertTrue(res.json['message'], "Loged out successfully")

    def test_login_unexisting_user(self):
        response = self.login_user("someone", "heistheone")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['message'], "No user found")

    def test_unmatching_creds(self):
        response = self.login_user("andrewhi", "ccccccc")
        self.assertEqual(response.status_code, 401)
