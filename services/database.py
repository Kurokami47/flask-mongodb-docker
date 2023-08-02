from pymongo import MongoClient
from bson import ObjectId  # Import the ObjectId class from bson module

class MongoDBService:
    def __init__(self, mongo_uri):
        self.mongo_uri = mongo_uri

    def create_user(self, data):
        # Connect to the MongoDB cluster
        mongo_client = MongoClient(self.mongo_uri)
        db = mongo_client.my_database
        users_collection = db.users

        # Create a new user and store it in the "users" collection
        user = User(data['name'], data['email'], data['password'])
        result = users_collection.insert_one(user.__dict__)
        user_id = str(result.inserted_id)
        return {'message': 'User created successfully', 'user_id': user_id}

    def get_users(self):
        # Connect to the MongoDB cluster
        mongo_client = MongoClient(self.mongo_uri)
        db = mongo_client.my_database
        users_collection = db.users

        # Get all users from the "users" collection
        users = users_collection.find()
        user_list = [user for user in users]
        for user in user_list:
            user['_id'] = str(user['_id'])
        return user_list

    def get_user_with_id(self, user_id):
        # Connect to the MongoDB cluster
        mongo_client = MongoClient(self.mongo_uri)
        db = mongo_client.my_database
        users_collection = db.users

        # Get a user by ID from the "users" collection
        user = users_collection.find_one({'_id': ObjectId(user_id)})  # Convert user_id to ObjectId
        if user:
            user['_id'] = str(user['_id'])  # Convert the ObjectId back to string
            return user
        return {'message': 'User not found'}

    def update_user(self, user_id, data):
        # Connect to the MongoDB cluster
        mongo_client = MongoClient(self.mongo_uri)
        db = mongo_client.my_database
        users_collection = db.users

        # Update a user by ID in the "users" collection
        updated_user = {'name': data['name'], 'email': data['email'], 'password': data['password']}
        result = users_collection.update_one({'_id': ObjectId(user_id)}, {'$set': updated_user})  # Convert user_id to ObjectId
        if result.modified_count > 0:
            return {'message': 'User updated successfully'}
        return {'message': 'User not found'}

    def delete_user(self, user_id):
        # Connect to the MongoDB cluster
        mongo_client = MongoClient(self.mongo_uri)
        db = mongo_client.my_database
        users_collection = db.users

        # Delete a user by ID from the "users" collection
        result = users_collection.delete_one({'_id': ObjectId(user_id)})  # Convert user_id to ObjectId
        if result.deleted_count > 0:
            return {'message': 'User deleted successfully'}
        return {'message': 'User not found'}
    
    
