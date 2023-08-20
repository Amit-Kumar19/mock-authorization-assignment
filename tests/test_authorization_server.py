import unittest
from authorization_server.auth import app as auth_app


class TestAuthorizationServer(unittest.TestCase):
    """
    Unit Test case for authorization_server/auth.py
    """

    def setUp(self):
        self.app = auth_app.test_client()

    def test_login(self):
        """ Test case to validate login of a valid user """

        response = self.app.post('/login', json={'username': 'user1', 'password': 'password1'})
        self.assertEqual(response.status_code, 200)

    def test_invalid_user(self):
        """ Test case to validate login of a invalid user """

        response = self.app.post('/login', json={'username': 'user', 'password': 'password1'})
        self.assertEqual(response.status_code, 401)

    def test_missing_username_or_password(self):
        """ Test case to validate missing username or password """

        response = self.app.post('/login', json={'username': 'user'})
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
