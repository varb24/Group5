from flask import Flask, jsonify
import pyodbc


# Database connection params
def get_db_connection():
    server = 'David'
    database = 'BooksAFewHundred'
    username = 'Ted'
    password = 'book'

    # Connecting to the database using PyODBC
    conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    return conn


# Function that gets ratings by user
def get_user_by_username(username):
    #Connect to database
    conn = get_db_connection()

    #Create a cursosr from the connection
    cursor = conn.cursor()

    #Search the SQL database for all data where the username in the link
    cursor.execute('SELECT * FROM UserData WHERE Username = ?', username)

    #Fetches the first row from the executed SQL query
    row = cursor.fetchone()

    #Closes the cursor and the database connection
    cursor.close()
    conn.close()

    #If there is nothing in that row, return nothing
    if row is None:
        return None
    #Creates a list of user details
    user = {
        'Username': row[0],
        'Password': row[1],
        'Name': row[2],
        'Emailaddress': row[3],
        'Homeaddress': row[4],
        'CreditCard': row[5]
    }
    return user

def handle_get_rating_request(userid):
    # Database connection
    conn = get_db_connection()
    # Retrieve the ratings for the specified user from database
    result = get_ratings_by_user(conn, userid)
    # Close the database connection
    conn.close()
    return jsonify(result)

def create_user(conn,user_data):
    cursor = conn.cursor()
    query = '''
        INSERT INTO UserData (Username, Password, Name, Emailaddress, Homeaddress)
        VALUES (?, ?, ?, ?, ?)
    '''
    values =(
        user_data['Username'],
        user_data['Password'],
        user_data.get('Name'),
        user_data.get('Email'),
        user_data.get('HomeAddress')
    )
    cursor.execute(query, values)
    conn.commit()

