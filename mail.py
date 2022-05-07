import smtplib
connection = smtplib.SMTP('smtp.gmail.com',587)
connection.ehlo() #to connect server with gmail
connection.starttls() # to start encryption
connection.login('#sender mail#', 'sender pwd') # enter email id and password.
connection.sendmail('#sender mail#','#reciver mail#','Subject: Write Your Subject \n\n Write here to send')
connection.quit()

def set_smtp_domain(serviseprovider):
    if serviseprovider == 'gmail':
        return 'smtp.gmail.com'
    elif serviseprovider == 'outlook' or serviseprovider == 'hotmail':
        return 'smtp-mail.outlook.com'
    elif serviseprovider == 'yahoo':
        return 'smtp-mail.yahoo.com'
print("Welcome You to send email through this program")
print("Please Enter your Email And Password : ")
e_mail , serviceProvider = get_mail()
password = input("Password : ")

