import smtplib, webbrowser
from smtplib import SMTP


def get_mail():
    Services = ['hotmail','gmail','yahoo','outlook']
    while True:
        mail_id = input("Enter Email : ")
        if '@' in mail_id and '.com' in mail_id:
            symbol_pos = mail_id.find("@")
            dotcom_pos = mail_id.find(".com")
            sp = mail_id[symbol_pos+1:dotcom_pos]
            if sp in Services:
                return mail_id , sp
                break
            else:
                print("We do not provide", sp , " service")
                continue
        else:
            print("Invali mail ID")
            continue

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
while True:
        try:
            smtpDomain = set_smtp_domain(serviceProvider)
            connect: SMTP = smtplib.SMTP(smtpDomain,587)
            connect.ehlo()
            connect.starttls()
            connect.login(e_mail,password)
        except:
            if serviceProvider == 'gmail':
                print("Login Unsuccessfull , Possibily Two Reasons")
                print("(1) You have typed Wrong inputs")
                print("(2) You are using gmail and you have allow some security settings")
                print("Do you want to allow")
                ans = input("yes or no? : " )
                if ans == "yes":
                    webbrowser.open("https://myaccount.google.com/lesssecureapps")
                else:
                    print("We can't open webpage without your permission you can go to https://myaccount.google.com/lesssecureapps")
                    print("Please retype your password also :")
                    e_mail , serviceProvider = get_mail()
                    password = input("Password : ")
                    continue
            else:
                print("Please retype your password also :")
                e_mail, serviceProvider = get_mail()
                password = input("Password : ")
                continue
        else:
            print("Login Successful")
            break


print("Please Type Receiver's Email Address : ")
receiverAddress , receiverSP = get_mail()
print("Now please type Subject And Message")
Subject = input("Subject : ")
Message = input("Message : ")
connect.sendmail(e_mail, receiverAddress, ("Subject : ",str(Subject),"\n\n",str(Message)))
print("Email Send Successfully")
connect.quit()
