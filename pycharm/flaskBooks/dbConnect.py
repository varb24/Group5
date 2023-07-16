import bookEntity
import pyodbc, requests
from flask import Flask, jsonify, request

app = Flask(__name__)
#Testing only
def connectLocal():
    connectInfo = ("Driver={SQL Server Native Client 11.0};"
                   "Server=DESKTOP-I7PCMKQ;"
                   "Database=BooksAFewHundred;"
                   "Trusted_Connection=yes;")

    connection = pyodbc.connect(connectInfo)
    cursor = connection.cursor()
    return cursor
#Patrick server
def get_db_connection():
    server = 'Hal'
    database = 'BooksAFewHundred'
    username = 'Group'
    password = 'book'

    # Connecting to the database using PyODBC
    conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = conn.cursor()
    return cursor
#Object pipes to DB
cursor = get_db_connection()
@app.route('/books/post/', methods=['POST'])
def postBook():
    book = bookEntity.Book(ISBN=request.json['ISBN'], bookName=request.json['name'],
                           bookDescription=request.json['description'], price=request.json['price'],
                           author=request.json['authorID'],
                           genre=request.json['genre'], publisher=request.json['publisherID'],
                           yearPublished=request.json['year'],
                           copies_sold=request.json['copiesSold'])

    # Will throw exception if there is duplicate data
    dbBoilerPlate = "INSERT INTO [dbo].[Book] ([ISBN],[Name],[description],[price],[genre],[authorID],[publisherID],[year],[copiesSold]) Values("
    # entry string is the entire command which tells the database to add information
    entryString = dbBoilerPlate + book.__str__() + ")"
    try:
        # sends the entryString command to the db.
        cursor.execute(entryString)
        cursor.commit()
    except pyodbc.IntegrityError:
        print("IntegrityError. Likely duplicate primary key value for book: " + book.__str__())
    return "PUT request successful!"


@app.route('/books/<isbn>', methods=['GET'])
def get_book(isbn):
    query = f"SELECT * FROM books_data WHERE isbn = '{isbn}'"
    cursor.execute(query)
    book = cursor.fetchone()
    if book:
        book_details = {
            'ISBN': book.ISBN, 'name': book.name, 'description': book.description, 'price': book.price,
            'genre': book.genre, 'author': book.authorID, 'publisherID': book.publisherID, 'year': book.year,
            'copies sold': book.copiesSold
        }
        return jsonify(book_details)
    else:
        return jsonify({'error': 'Book not found'}), 404


@app.route('/')
def index():
    print('This message will be printed in the console.')
    return 'Hello, Flask!'


if __name__ == '__main__':
    app.run(debug=True)
