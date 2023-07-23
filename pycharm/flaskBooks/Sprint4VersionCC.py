from flask import Flask, jsonify, request
import pyodbc

app = Flask(__name__)

server = '(local)'
database = 'BooksAFewHundred'
username = 'Ted'
password = 'book'

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)


@app.route('/books/<string:genre>', methods=['GET'])
def get_books_by_genre(genre):
    cursor = conn.cursor()
    query = 'SELECT ISBN, Name FROM Book WHERE ' \
            'Genre = ?'
    cursor.execute(query, genre)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        item = {
            'Name': row[1],
        }
        result.append(item)

    return jsonify(result)


@app.route('/books/top-sellers', methods=['GET'])
def get_top_sellers():
    cursor = conn.cursor()
    query = 'SELECT TOP 10 ISBN, Name FROM Book ' \
            'ORDER BY CopiesSold DESC'
    cursor.execute(query)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        item = {
            'Name': row[1],
        }
        result.append(item)

    return jsonify(result)


@app.route('/books/rating', methods=['GET'])
def get_books_by_rating():
    rating = request.args.get('rating')
    if rating is None:
        return jsonify({'error': 'Rating parameter is missing.'}), 400

    try:
        rating = int(rating)
    except ValueError:
        return jsonify({'error': 'Rating must be an integer.'}), 400

    cursor = conn.cursor()
    query = 'SELECT b.Name FROM Rating r LEFT JOIN Book b ON b.ISBN = r.BookID WHERE Rating >= ?'
    cursor.execute(query, rating)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        item = {
            'Name': row[0],
        }
        result.append(item)

    return jsonify(result)


@app.route('/books/discount', methods=['PUT', 'PATCH'])
def discount_books_by_publisher():
    data = request.get_json()
    discount_percent = data.get('discount_percent')
    publisher = data.get('publisher')

    if not discount_percent or not publisher:
        return jsonify({'error': 'Discount percent and publisher are required parameters.'}), 400

    try:
        discount_percent = float(discount_percent)
    except ValueError:
        return jsonify({'error': 'Discount percent must be a valid number.'}), 400

    cursor = conn.cursor()
    query = 'Update book set Price = (Price - (Price * ?)) FROM Book b LEFT JOIN Publisher p ON b.PublisherID = ' \
            'p.PublisherID WHERE p.PublisherID = ?'
    cursor.execute(query, discount_percent, publisher)
    conn.commit()

    return jsonify({'message': 'Books discounted successfully.'})


if __name__ == '__main__':
    app.run()
