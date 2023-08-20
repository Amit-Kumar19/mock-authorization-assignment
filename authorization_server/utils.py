import jwt
import datetime
import logging


def generate_jwt_token(username, secret_key):
    """
    Generate a JWT token with a user's username.
    Args:
        username (str): The user's username.
        secret_key (str): Secret key
    Returns:
        str: The generated JWT token.
    """

    try:
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }

        jwt_token = jwt.encode(payload, secret_key, algorithm='HS256')
        return jwt_token

    except Exception as e:
        logging.error(f"Error in generating token: {e}")