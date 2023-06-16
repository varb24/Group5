from flask import Flask, jsonify
import pyodbc


# Database connection params
def get_db_connection():
    server = 'localhost'
    database = 'BooksAFewHundred'
    username = 'Group'
    password = 'book'

    # Connecting to the database using PyODBC
    conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    return conn


# Function that gets ratings by user
def get_ratings_by_user(conn, userid):
    # Create a cursor from the connection
    cursor = conn.cursor()
    # Execute the SQL query
    cursor.execute('SELECT RatingId, Rating, BookId, UserId FROM Rating WHERE UserId = ?', userid)
    # Fetch all rows from the executed SQL query
    rows = cursor.fetchall()

    # Process rows into a list of dictionaries to be returned
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
    # Database connection
    conn = get_db_connection()
    # Retrieve the ratings for the specified user from database
    result = get_ratings_by_user(conn, userid)
    # Close the database connection
    conn.close()
    return jsonify(result)
