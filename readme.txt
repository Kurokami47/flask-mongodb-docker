# Sample Flask Application - README

This is a simple Flask application with CRUD operations (Create, Read, Update, Delete) using MongoDB Atlas as the database. The application allows you to create, read, update, and delete user data.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Testing the Application](#testing-the-application)
- [Environment Variables](#environment-variables)

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.6 or higher
- pip package manager
- MongoDB Atlas account (for database access)

## Setup

1. Clone the repository to your local machine.

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate    # On Windows, use "venv\Scripts\activate" instead
   ```

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory of the project with the following contents:
   ```
   DEBUG=True
   MONGO_URI=mongodb+srv://admin:3214@practice.samqo0n.mongodb.net/?retryWrites=true&w=majority
   ```

## Running the Application

1. Set the following environment variables (these are already specified in the .env file):

   - `FLASK_ENV`: Set it to `development` for development mode or `production` for production mode.
   Example: `FLASK_ENV=development`

   - `FLASK_APP`: The main application file (app.py).
   Example: `FLASK_APP=app.py`

2. Run the application:
   ```
   flask run
   ```

3. The application should now be running locally. Access it at `http://localhost:5000` in your web browser.
   Populating MongoDB with Dummy Data
   The application provides a script called generatedummy_data.py that uses the Faker library to populate the MongoDB database with dummy user data. You can run this script to generate random user records in your MongoDB database.
   To run the script, make sure your virtual environment is activated, and the MongoDB URI in the .env file is correctly set to your MongoDB Atlas cluster.
   Run the following command to populate MongoDB with dummy data:

   ```
   python generatedummy_data.py
   ```




## Testing the Application

To test the application, you can use Postman or any other API testing tool. Use the following endpoints to interact with the application:

- `GET /users`: Fetch all users from the database.
- `GET /users/<user_id>`: Fetch a specific user by their ID.
- `POST /users`: Create a new user. Send a JSON payload with user data.
- `PUT /users/<user_id>`: Update an existing user by their ID. Send a JSON payload with updated user data.
- `DELETE /users/<user_id>`: Delete a user by their ID.

## Note

If you are using MongoDB Atlas, you do not need to set up a local MongoDB container. MongoDB Atlas handles the database hosting and management for you in the cloud. Simply configure your application to use the MongoDB Atlas connection string to interact with the database. The `.env` file provided in the project already contains the necessary `MONGO_URI` variable for MongoDB Atlas access.