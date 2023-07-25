from flask import Flask, jsonify
import pyodbc

# Database connection params
def get_db_connection():
    server = 'LAPTOP-OJUP0D6T'
    database = 'BooksAFewHundred'
    username = 'Ted'
    password = 'book'

    # Connecting to the database using PyODBC
    conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    return conn


# Feature 1
def create_user(conn, user_data):
    # Create a cursor from the connection

    cursor = conn.cursor()

    # Set up the query
    query = 'INSERT INTO LogUser (UserName, Password, Name, Email, HomeAddress) VALUES (?, ?, ?, ?, ?)'
    # Provides the values for each column in the table
    values = (
        user_data['Username'],
        user_data['Password'],
        user_data.get('Name'),
        user_data.get('Email'),
        user_data.get('HomeAddress')
    )
    # Executes the query
    cursor.execute(query, values)
    conn.commit()

# Feature 2: Helper Functions
def get_user_by_username(username):
    # Connect to database
    conn = get_db_connection()

    # Create a cursor from the connection
    cursor = conn.cursor()

    # Search the SQL database for all data where the username is found
    cursor.execute('SELECT UserName, Password, Name, Email, HomeAddress, CreditCard FROM LogUser WHERE UserName = ?', username)

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



# Feature 3
def update_user_data(username, data):
    # Database connection and cursor
    conn = get_db_connection()
    cursor = conn.cursor()
    # Starts the query
    query = ''' UPDATE LogUser SET '''
    values = []

    for field, value in data.items():
        # Reverted to old code, checks if the email field is being edited.
        if field != 'Email':
            query += f"{field} = ?, "
            values.append(value)
    # Finishes up the query
    query = query.rstrip(', ') + ''' Where Username = ? '''
    values.append(username)
    # Executes the query
    cursor.execute(query, values)
    conn.commit()
    conn.close()

# Feature 4
def credit_card_creation(username, credit_card_data):
    # Establish connection
    conn = get_db_connection()
    # Sets up the query
    query = 'UPDATE LogUser SET CreditCard = ? WHERE Username = ?'

    # Exucutes the query
    conn.execute(query, (credit_card_data, username))

    conn.commit()

    conn.close()
