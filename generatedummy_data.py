from faker import Faker
from pymongo import MongoClient

# Set the MongoDB Atlas URI and database name
# Replace 'your_username', 'your_password', and 'your_cluster_name' with your Atlas credentials
# Use any valid database name of your choice (e.g., "my_database")
MONGO_URI = 'mongodb+srv://admin:3214@practice.samqo0n.mongodb.net/?retryWrites=true&w=majority'
mongo = MongoClient(MONGO_URI)
db = mongo.my_database  # Replace 'my_database' with your chosen database name

# Define the User Model (as mentioned before)
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# Function to generate dummy data for the User resource
def generate_dummy_data(num_records):
    fake = Faker()

    for _ in range(num_records):
        name = fake.name()
        email = fake.email()
        password = fake.password()

        user = User(name, email, password)
        print(user.__dict__)
        db.users.insert_one(user.__dict__)

if __name__ == '__main__':
    num_records = 50
    generate_dummy_data(num_records)
    print(f'{num_records} dummy records created successfully.')
