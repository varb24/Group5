from flask import Flask, jsonify
import pyodbc
import helperFunctions

app = Flask(__name__)


# Define a route for getting data by user id
@app.route('/rating/<int:userid>', methods=['GET'])
def get_data_by_id(userid):
    helperFunctions.handle_get_rating_request(userid)
    #Call the 'handle_get_rating_request' function from the 'helperFunctions'
    #Handles the GET request for ratings by a user

if __name__ == '__main__':
    app.run()