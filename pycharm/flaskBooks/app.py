from flask import Flask, jsonify
import pyodbc
import helperFunctions

app = Flask(__name__)



@app.route('/rating/<int:userid>', methods=['GET'])
def get_data_by_id(userid):
    helperFunctions.handle_get_rating_request(userid)
    #

if __name__ == '__main__':
    app.run()