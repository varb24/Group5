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
    # Connect to database
    conn = get_db_connection()

    # Create a cursosr from the connection
    cursor = conn.cursor()

    # Search the SQL database for all data where the username in the link
    cursor.execute('SELECT * FROM UserData WHERE Username = ?', username)

    # Fetches the first row from the executed SQL query
    row = cursor.fetchone()
    # Closes the cursor and the database connection
    cursor.close()
    conn.close()

    # If there is nothing in that row, return nothing
    if row is None:
        return None
    # Creates a list of user details
    user = {
        'Username': row[0],
        'Password': row[1],
        'Name': row[2],
        'Emailaddress': row[3],
        'Homeaddress': row[4],
        'CreditCard': row[5]
    }
    return user


def create_user(conn, user_data):
    # Create a cursosr from the connection

    cursor = conn.cursor()

    # Inserts the data from UserData into the following collumn fields
    query = ''' INSERT INTO UserData (Username, Password, Name, Emailaddress, Homeaddress)VALUES (?, ?, ?, ?, ?) '''
    values = (
        user_data['Username'],
        user_data['Password'],
        user_data.get('Name'),
        user_data.get('Email'),
        user_data.get('HomeAddress')
    )
    cursor.execute(query, values)
    conn.commit()


def update_user_data(username, data):
    # Database connection and cursor
    conn = get_db_connection()
    cursor = conn.cursor()
    query = ''' UPDATE UserData SET '''
    values = []
    #
    for key, value in data.items():
        if key.lower() != 'emailaddress':
            query += f"{key} = ?, "
            values.append(value)

    query = query.rstrip(', ') + ''' Where Username = ? '''
    values.append(username)

    cursor.execute(query, values)
    conn.commit()
    conn.close()


def credit_card_creation(username, credit_card_data):
    conn = get_db_connection()

    query = 'UPDATE UserData SET CreditCard = ? WHERE Username = ?'

    conn.execute(query, (credit_card_data, username))

    conn.commit()

    conn.close()
