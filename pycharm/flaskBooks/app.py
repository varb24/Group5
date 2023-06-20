from flask import Flask, jsonify, request
import pyodbc
import helperFunctions

app = Flask(__name__)


# Define a route for getting data by user id
@app.route('/rating/<int:userid>', methods=['GET'])
def get_data_by_id(userid):
    return helperFunctions.handle_get_rating_request(userid)
    #Call the 'handle_get_rating_request' function from the 'helperFunctions'
    #Handles the GET request for ratings by a user

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

    return jsonify({'message': 'User created successfilly'}), 201

if __name__ == '__main__':
    app.run()