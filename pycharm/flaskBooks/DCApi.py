from flask import Flask, jsonify, request
import pyodbc
import helperFunctions

app = Flask(__name__)


# Define a route for getting data by the user's username. Get method because
@app.route('/users/<username>', methods=['GET'])
# Rest API Action #2: Retrieve A User's fields by their username
def get_user_by_username(username):
    # Calls upon the get user by username function
    user = helperFunctions.get_user_by_username(username)
    # Self explainitory, if we can't find anything on that user, we print that the user is not found
    if user is None:
        return jsonify({'message': 'User is not found'}), 404
    # returns the data on the user, from the list made in get_user_by_username in helpferfuntions.py
    return jsonify(user)


# Rest API Action #1: Create a User
@app.route('/users', methods=['POST'])
def create_user():
    # Get the user data from the request body
    user_data = request.json

    # Database connection
    conn = helperFunctions.get_db_connection()

    # Create the user in the database
    helperFunctions.create_user(conn, user_data)

    # Close the database connection
    conn.close()

    return jsonify({'message': 'User created successfully'}), 201


@app.route('/users/<username>', methods=['PUT', 'PATCH'])
def update_user_data(username):
    # Get the user data from the request body
    data = request.json
    helperFunctions.update_user_data(username, data)

    return jsonify({'message': 'User information updated successfully'}), 201


@app.route('/users/<username>', methods=['POST'])
def credit_card_creation(username):
    data = request.json
    credit_card_data = data.get('CreditCard')

    helperFunctions.credit_card_creation(username, credit_card_data)

    return jsonify({'message': 'Credit Card information updated successfully'}), 201


if __name__ == '__main__':
    app.run()
