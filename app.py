from flask import Flask
from flask_restful import Api, Resource, reqparse
from services.database import MongoDBService
from dotenv import load_dotenv
import os
import custom_logger

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Load environment variables for Flask configuration
app.config['DEBUG'] = os.environ.get('DEBUG', False)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/my_database')

mongo_service = MongoDBService(app.config['MONGO_URI'])

# Define the request parser for user data
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True, help='Name field cannot be blank.')
user_parser.add_argument('email', type=str, required=True, help='Email field cannot be blank.')
user_parser.add_argument('password', type=str, required=True, help='Password field cannot be blank.')


class UserResource(Resource):
    def get(self, user_id):
        result = mongo_service.get_user_with_id(user_id)
        return result

    def put(self, user_id):
        data = user_parser.parse_args()
        result = mongo_service.update_user(user_id, data)
        custom_logger.logging.info('User updated: {}'.format(user_id))  # Use the logging instance from custom_logger
        return result

    def delete(self, user_id):
        result = mongo_service.delete_user(user_id)
        custom_logger.logging.info('User deleted: {}'.format(user_id))  # Use the logging instance from custom_logger
        return result


class UserListResource(Resource):
    def get(self):
        result = mongo_service.get_users()
        return result

    def post(self):
        data = user_parser.parse_args()
        result = mongo_service.create_user(data)
        custom_logger.logging.info('New user created: {}'.format(data['name']))  # Use the logging instance from custom_logger
        return result


api = Api(app)

# Add the resources to the API
api.add_resource(UserResource, '/users/<string:user_id>')
api.add_resource(UserListResource, '/users')


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
