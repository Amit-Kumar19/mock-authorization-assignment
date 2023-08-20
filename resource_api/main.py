from flask import Flask, request
import jwt
import logging

from resource_api.sample_data import sample_resource_data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this in production

# Add logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/get_details', methods=['GET'])
def get_user_details():
    """
    Access a protected route to get user details with a valid JWT token.
    Returns:
        JSON response: {'message': 'Hello, username! You have access to this protected API.',
                        'data': 'User valid Data'}
                      or {'message': 'Token is missing'} or {'message': 'Token has expired'}
                      or {'message': 'Invalid token'}
        Status code:
                200 - Successful response
                401 - Error due to token expiry/missing/invalid
                500 - Any other application exceptions
    """

    try:
        token = request.headers.get('Authorization')

        if not token:
            return {'message': 'Token is missing'}, 401

        try:
            decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            username = decoded_token['username']

            return {'message': f'Hello, {username}! You have access to this protected API.',
                    'data': f'{sample_resource_data[username]}'}, 200

        except jwt.ExpiredSignatureError:
            return {'message': 'Token has expired'}, 401
        except jwt.InvalidTokenError:
            return {'message': 'Invalid token'}, 401

    except Exception as e:
        logging.error(f"Error in Accessing Resource User details API: {e}")
        return {'message': 'Internal Server Error'}, 500


if __name__ == '__main__':
    logging.info("Starting Resource API")
    app.run(debug=True, port=5001)
