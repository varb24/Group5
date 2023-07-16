USE [BooksAFewHundred]
GO

INSERT INTO [dbo].[UserData]
           ([Username]
           ,[Password]
           ,[Name]
           ,[Emailaddress]
           ,[Homeaddress]
           ,[CreditCard])
     VALUES
           ('johndoe123'
           ,'p@ssw0rd!'
           ,'John Doe'
           ,'johndoe123@example.com'
           ,'123 Fake Street, Anytown, USA'
           ,'4111 1111 1111 1111'),
		   ('sarasmith22'
		   ,'securePassword123'
		   ,'Sara Smith'
		   ,'sara.smith22@example.com'
		   ,'456 Mock Avenue, Cityville, USA'
		   ,'5555 5555 5555 4444'),
		   ('mikerobinson'
		   ,'mySecretPass'
		   ,'Mike Robinson'
		   ,'mike.robinson@example.com'
		   ,'789 Faux Road, Townsville, USA'
		   ,'3782 822463 10005'),
		   ('emilyjones78'
		   ,'pass123word'
		   ,'Emily Jones'
		   ,'emily.jones78@example.com'
		   ,'321 Counterfeit Lane, Villageton, USA'
		   ,'6011 6011 6011 6611')

GO


