from flask import Flask, request
import logging

from authorization_server.utils import generate_jwt_token
from authorization_server.mock_users import MockUsers

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # For simplicity its hardcoded

# Add logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# get dummy users id and password, ideally should be fetched from a DB
users = MockUsers().users


@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate a user and issue a JWT token upon successful login.
    Returns:
        JSON response: {'token': 'generated_token'} or {'message': 'Invalid credentials'} with status code
        200 - Successful validation
        401 - Invalid Validation, Username/Password missing
        500 - Any other exceptions
    """

    try:
        data = request.json
        username = data['username']
        password = data['password']

        # validate if users exits or not, if yes return a JWT with 200 response code
        if username in users and users[username] == password:
            token = generate_jwt_token(username, app.config['SECRET_KEY'])
            return {'token': token}, 200

        return {'message': 'Invalid credentials'}, 401

    except KeyError as err:
        logging.error(f"Error in login, username or password missing: {err}")
        return {'message': 'Missing Username of Password'}, 401

    except Exception as err:
        logging.error(f"Error in login: {err}")
        return {'message': 'Internal Server Error'}, 500


if __name__ == '__main__':
    logging.info("Starting Authorization Server")
    app.run(debug=True, port=5000)
