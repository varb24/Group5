from flask import Flask, jsonify
import pyodbc
def get_db_connection():
    server = 'Hal'
    database = 'BooksAFewHundred'
    username = 'Group'
    password = 'book'

    conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    return conn
def get_ratings_by_user(conn, userid):
    cursor = conn.cursor()
    cursor.execute('SELECT RatingId, Rating, BookId, UserId FROM Rating WHERE UserId = ?', userid)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append({
            'RatingId': row[0],
            'Rating': row[1],
            'BookId': row[2],
            'UserId': row[3]
        })
    return result

def handle_get_rating_request(userid):
    conn = get_db_connection()
    result = get_ratings_by_user(conn, userid)
    conn.close()
    return jsonify(result)
