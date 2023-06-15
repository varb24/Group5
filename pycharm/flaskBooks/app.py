from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

server = 'Hal'
database = 'BooksAFewHundred'
username = 'Group'
password = 'book'


conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)


@app.route('/rating/<int:userid>', methods=['GET'])
def get_data_by_id(userid):
    cursor = conn.cursor()
    query = 'SELECT RatingId, Rating, BookId, UserId FROM Rating WHERE UserId = ?'
    cursor.execute(query, userid)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        item = {
            'RatingId': row[0],
            'Rating': row[1],
            'BookId': row[2],
            'UserId': row[3],
        }
        result.append(item)

    return jsonify(result)


if __name__ == '__main__':
    app.run()
