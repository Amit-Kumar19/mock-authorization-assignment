import argparse

import requests
import logging

AUTH_SERVER_URL = 'http://localhost:5000'  # Authorization server URL
RESOURCE_API_URL = 'http://localhost:5001'  # Resource API URL

# Add logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def login(username, password):
    """
    Authenticate a user and obtain a JWT token.
    Args:
        username (str): The user's username.
        password (str): The user's password.
    Returns:
        str: The JWT token if authentication is successful, otherwise None.
    """
    try:
        data = {'username': username, 'password': password}
        response = requests.post(f'{AUTH_SERVER_URL}/login', json=data)

        if response.status_code == 200:
            return response.json().get('token')
        else:
            logging.error(f"Login failed: {response.text}")
            return None

    except Exception as e:
        logging.error(f"Error in login: {e}")
        return None


def get_user_details(token):
    """
    Access protected data using a JWT token.
    Args:
        token (str): The JWT token.
    Returns:
        dict: The protected data if access is granted, otherwise Error Msg.
    """

    try:
        headers = {'Authorization': token}
        response = requests.get(f'{RESOURCE_API_URL}/get_details', headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Failed to get protected data: {response.text}")

    except Exception as e:
        logging.error(f"Error in get_protected_data: {e}")


def main():
    """ Main entry point of client code"""

    parser = argparse.ArgumentParser(description='Client for Authentication and Authorization System')
    parser.add_argument('--username', required=True, help='The username to login')
    parser.add_argument('--password', required=True, help='The password to login')
    args = parser.parse_args()

    username = args.username
    password = args.password

    response = login(username, password)
    if response:
        logging.info('Login successful!')
        user_details = get_user_details(response)
        if user_details:
            logging.info(f'Protected data:, {user_details}')
    else:
        logging.warning('Login failed! Try Again')


if __name__ == '__main__':
    main()
