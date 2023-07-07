from flask import Flask, jsonify, request
import pyodbc
import datetime


app = Flask(__name__)

server = 'HAL'
database = 'BooksAFewHundred'
username = 'Group'
password = 'book'

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()


@app.route('/rating', methods=['GET', 'POST'])
def add_rating(userid=None):
    data = request.get_json()
    rating = data['rating']
    user_id = data['user_id']
    book_id = data['book_id']
    created_date = datetime.datetime.now()

    query = "INSERT INTO Rating (rating,BookId,UserId,CreatedDate) VALUES(?,?,?,?) "
    cursor.execute(query, (rating, book_id, user_id, created_date))
    conn.commit()

    response = jsonify({"message": "Rating added successfully"})
    response.headers['Accept'] = 'application/json'

    return response


@app.route('/comment', methods=['GET', 'POST'])
def add_comment():
    data = request.get_json()
    comment = data['comment']
    book_id = data['book_id']
    user_id = data['user_id']
    created_date = datetime.datetime.now()

    # Insert the comment into the database
    query = "INSERT INTO Comment (Comment, BookId, UserId,CreatedDate) VALUES (?,?,?,?)"
    cursor.execute(query, (comment, book_id, user_id, created_date))
    conn.commit()

    response = jsonify({"message": "Rating added successfully"})
    response.headers['Accept'] = 'application/json'

    return response


@app.route('/book-comments/<book_id>', methods=['GET'])
def get_book(book_id):
    # Fetch the book details from the database
    query = "SELECT b.Name,Comment FROM Comment c left join Book b on b.ISBN = c.BookId where c.BookId = ?"
    cursor.execute(query, book_id)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        item = {
            'book': row[0],
            'comment': row[1]
        }
        result.append(item)

    return jsonify(result)


@app.route('/average-book/<book_id>', methods=['GET'])
def get_book_rating(book_id):
    query = "SELECT avg(r.Rating) as rating, b.name FROM Rating r left join Book b on b.ISBN = r.BookId where r.BookId = ? group by r.Rating, b.name"
    cursor.execute(query, book_id)
    average_rating = cursor.fetchone()

    return jsonify({'rating': average_rating[0], 'book': average_rating[1]})


if __name__ == '__main__':
    app.run()
