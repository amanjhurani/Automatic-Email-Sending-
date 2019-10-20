import smtplib
connection = smtplib.SMTP('smtp.gmail.com',587)
connection.ehlo() #to connect server with gmail
connection.starttls() # to start encryption
connection.login('#sender mail#', 'sender pwd') # enter email id and password.
connection.sendmail('#sender mail#','#reciver mail#','Subject: Write Your Subject \n\n Write here to send')
connection.quit()
