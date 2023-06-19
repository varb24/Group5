import pyodbc


def get_db_connection():
    server = 'David'
    database = 'BooksAFewHundred'
    username = 'Ted'
    password = 'book'

    # Connecting to the database using PyODBC
    conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    return conn


conn = get_db_connection()
cursor = conn.cursor()
cursor.execute("SELECT 1")
result = cursor.fetchone()
print(result)
conn.close()
