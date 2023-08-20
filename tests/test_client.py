import unittest
from client.main import login, get_user_details


class TestClient(unittest.TestCase):
    """
    Unit Test case for client/main.py
    """

    def test_login(self):
        """ Test case to validate login of a user"""

        response = login('user1', 'password1')
        self.assertIsNotNone(response)

    def test_invalid_login(self):
        """ Test case to validate login failure"""

        response = login('user1', 'password')
        self.assertIsNone(response)

    def test_get_user_details(self):
        """ Test case to validate failure of getting data"""

        protected_data = get_user_details('invalid_token_here')
        self.assertIsNone(protected_data)


if __name__ == '__main__':
    unittest.main()
