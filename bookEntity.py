import requests


class Book:
    # All arguments must be strings(ints provide no benefits, we won't be doing any math with these numbers
    def __init__(self, ISBN: str, bookName: str, bookDescription: str, price: str, author: str, genre: str,
                 publisher: str, yearPublished: int, copiesSold: str):
        self.ISBN = ISBN
        self.bookName = bookName
        self.bookDescription = bookDescription
        self.price = price
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.yearPublished = yearPublished
        self.copiesSold = copiesSold




    # Overwritten print to string method to return SQL friendly string
    def __str__(self):
        output = ""
        # iterates through all object attributes and adds them to a string
        for attr, value in self.__dict__.items():
            output += "'%s'," % value
        # Removes the one extra ',' at the end of the string
        output = output.rstrip(output[-1])
        return output

    #posts object to a website
    def post(self, url: str):
        responce = requests.post(url, data = self)
        return responce
