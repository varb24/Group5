# Using bookEntity as a template
import requests
class User:
    #This will contain all of the user data
    def __int__(self, username: str, password: str, name: str, email: str, address: str,
                 home_address: str, credit_card: str):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.address = address
        self.home_address = home_address
        self.credit_card = credit_card

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
