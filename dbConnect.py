import bookEntity
import userEntity
import pyodbc


def postBook(book: bookEntity.Book):
    ## Connects to SQL server
    connectInfo = ("Driver={SQL Server Native Client 11.0};"
                   "Server=DESKTOP-I7PCMKQ;"
                   "Database=books;"
                   "Trusted_Connection=yes;")

    connection = pyodbc.connect(connectInfo)
    cursor = connection.cursor()
    ##
    # Will throw exception if there is duplicate data
    dbBoilerPlate = "INSERT INTO [dbo].[books_data] ([ISBN],[name],[description],[price],[genre],[author],[publisher],[year],[copies_sold]) Values("
    entryString = dbBoilerPlate + book.__str__() +")"
    try:
        cursor.execute(entryString)
        cursor.commit()
    except pyodbc.IntegrityError:
        print("IntegrityError. Likely duplicate primary key value for book: " + book.__str__())

def PostUser(user: userEntity.User):
    connectInfo = ( "Driver={SQL Server Native Client 11.0};"
                   "Server=DESKTOP-I7PCMKQ;"
                   "Database=users;"
                   "Trusted_Connection=yes;"

    )
    connection = pyodbc.connect(connectInfo)
    cursor = connection.cursor()

    dbBoilerPlate = "INSERT INTO [dbo].[users_data] ([Username],[Password],[Name],[Email],[Address],[HomeAddress],[CreditCard]) Values("
    entryString = dbBoilerPlate + user.__str__() + ")"

    try:
        cursor.execute(entryString)
        cursor.commit()
    except pyodbc.IntegrityError:
        print("IntegrityError. Likely duplicate primary key value for user: " + user.__str__())


a = bookEntity.Book('144', 'Nnames', 'Wow', 'newbook', '42', 'Scifi', 'Me', '1986', '1324934')

postBook(a)
# addBook()
