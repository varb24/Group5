import json
from flask import Flask
import requests



class Book:
    # All arguments must be strings(ints provide no benefits, we won't be doing any math with these numbers
    def __init__(self, ISBN: str, bookName: str, bookDescription: str, price: str, author: str, genre: str,
                 publisher: str, yearPublished: int, copies_sold: str):
        self.ISBN = ISBN
        self.bookName = bookName
        self.bookDescription = bookDescription
        self.price = price
        self.genre = genre
        self.author = author
        self.publisher = publisher
        self.yearPublished = yearPublished
        self.copies_sold = copies_sold



    # Overwritten print to string method to return SQL friendly string
    def __str__(self):
        output = ""
        # iterates through all object attributes and adds them to a string
        for attr, value in self.__dict__.items():
            output += "'%s'," % value
        # Removes the one extra ',' at the end of the string
        output = output.rstrip(output[-1])
        return output


    #returns JSON compatible string of object's attributes
    def json(self):
        output = "{"
        for attr, value in self.__dict__.items():
            output += f'"{attr}": "{value}",'
        # Removes the one extra ',' at the end of the string
        output = output.rstrip(output[-1]) +  '}'
        return output

class Author:
    def __init__(self, firstName: str, lastName: str, description: str, biography: str, publisherID: int):
        self.firstName = firstName
        self.lastName = lastName
        self.biography = biography
        self.description = description
        self.publisher = publisherID

    def __str__(self):
        output = ""
        # iterates through all object attributes and adds them to a string
        for attr, value in self.__dict__.items():
            output += "'%s'," % value
        # Removes the one extra ',' at the end of the string
        output = output.rstrip(output[-1])
        return output

    #returns JSON compatible string of object's attributes
    def json(self):
        output = "{"
        for attr, value in self.__dict__.items():
            output += f'"{attr}": "{value}",'
        # Removes the one extra ',' at the end of the string
        output = output.rstrip(output[-1]) +  '}'
        return output
