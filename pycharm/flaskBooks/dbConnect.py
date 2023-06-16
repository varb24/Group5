import bookEntity
import pyodbc, requests
from flask import Flask, jsonify, request

app = Flask(__name__)

connectInfo = ("Driver={SQL Server Native Client 11.0};"
               "Server=DESKTOP-I7PCMKQ;"
               "Database=books;"
               "Trusted_Connection=yes;")

connection = pyodbc.connect(connectInfo)
cursor = connection.cursor()


@app.route('/books/put/', methods=['POST'])
def postBook():
    print(request.json['ISBN'])
    book = bookEntity.Book(ISBN=request.json['ISBN'], bookName=request.json['name'],
                           bookDescription=request.json['description'], price=request.json['price'],
                           author=request.json['author'],
                           genre=request.json['genre'], publisher=request.json['publisher'],
                           yearPublished=request.json['year'],
                           copies_sold=request.json['copies_sold'])
    print(book.__str__())
    # Will throw exception if there is duplicate data
    dbBoilerPlate = "INSERT INTO [dbo].[books_data] ([ISBN],[Name],[description],[price],[genre],[author],[publisher],[year],[copies_Sold]) Values("
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
            'genre': book.genre, 'publisher': book.publisher, 'year': book.year, 'copies sold': book.copies_sold
        }
        return jsonify(book_details)
    else:
        return jsonify({'error': 'Book not found'}), 404


@app.route('/')
def index():
    print('This message will be printed in the console.')
    return 'Hello, Flask!'


# creates a book object(This is where you would randomly generate the data.

a = bookEntity.Book('142', 'Nnames', 'Wow', 'newbook', '42', 'Scifi', 'Me', '1986', '1324934')
# postBook(a)
# get_book2(144)
# print(get_book2('144'))

if __name__ == '__main__':
    app.run(debug=True)
