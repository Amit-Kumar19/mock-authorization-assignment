import unittest
from resource_api.main import app as resource_app


class TestResourceAPI(unittest.TestCase):
    """
    Unit Test case for resource_api/main.py
    """

    def setUp(self):
        self.app = resource_app.test_client()

    def test_get_user_details(self):
        """ Test case to validate incorrect token passed """

        response = self.app.get('/get_details', headers={'Authorization': 'valid_token_here'})
        self.assertEqual(response.status_code, 401)

    def test_token_invalid(self):
        """ Test case to validate missing token """

        response = self.app.get('/get_details', headers={})
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
