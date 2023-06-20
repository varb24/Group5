from flask import Flask, jsonify, request
import pyodbc
import helperFunctions

app = Flask(__name__)


# Define a route for getting data by the user's username. Get method because
@app.route('/users/<username>', methods=['GET'])

def get_user_by_username(username):
    user = helperFunctions.get_user_by_username(username)
    #Self explainitory, if we can't find anything on that user, we print that the user is not found
    if user is None:
        return jsonify({'message': 'User is not found'}), 404
    #returns the data on the user, from the list made in get_user_by_username in helpferfuntions.py
    return jsonify(user)

@app.route('/api/users',methods =['POST'])
def create_user():
    #Get the user data from the request body
    user_data = request.json

    #Database connection
    conn = helperFunctions.get_db_connection()

    #Create the user in the database
    helperFunctions.create_user(conn, user_data)

    #close the database connection
    conn.close()

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/api/users',methods = ['PATCH'])
def update_user_data(username):
    # Get the user data from the request body
    data = request.json
    helperFunctions.update_user_request(username, data)

    return jsonify({'message': 'User information updated successfully'}), 201

if __name__ == '__main__':
    app.run()