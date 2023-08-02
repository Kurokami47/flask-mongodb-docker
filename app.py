from flask import Flask, jsonify, request
from services.database import MongoDBService
from dotenv import load_dotenv
import os
import custom_logger  
from model import User

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Load environment variables for Flask configuration
app.config['DEBUG'] = os.environ.get('DEBUG', False)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/my_database')

mongo_service = MongoDBService(app.config['MONGO_URI'])

# Route to create a new user and store it in the "users" collection
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    result = mongo_service.create_user(data)
    custom_logger.logging.info('New user created: {}'.format(data['name']))  # Use the logging instance from custom_logger
    return jsonify(result), 201

# Route to get all users from the "users" collection
@app.route('/users', methods=['GET'])
def get_users():
    result = mongo_service.get_users()
    return jsonify(result)

# Route to get a user by ID from the "users" collection
@app.route('/users/<string:user_id>', methods=['GET'])
def get_user_with_id(user_id):
    result = mongo_service.get_user_with_id(user_id)
    return jsonify(result)

# Route to update a user by ID in the "users" collection
@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    result = mongo_service.update_user(user_id, data)
    custom_logger.logging.info('User updated: {}'.format(user_id))  # Use the logging instance from custom_logger
    return jsonify(result)

# Route to delete a user by ID from the "users" collection
@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = mongo_service.delete_user(user_id)
    custom_logger.logging.info('User deleted: {}'.format(user_id))  # Use the logging instance from custom_logger
    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
