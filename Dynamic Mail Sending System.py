import smtplib, webbrowser
from smtplib import SMTP


def get_mail():
    Services = ['hotmail','gmail','yahoo','outlook']
    while True:
        mail_id = input("Enter Your E-mail Id : ")
        if '@' in mail_id and '.com' in mail_id:
            symbol_pos = mail_id.find("@")
            dotcom_pos = mail_id.find(".com")
            sp = mail_id[symbol_pos+1:dotcom_pos]
            if sp in Services:
                return mail_id , sp
                break
            else:
                print("We Don't provide : ", sp , " service")
                continue
        else:
            print("Invalid E-mail Id")
            continue

def set_smtp_domain(serviseprovider):
    if serviseprovider == 'gmail':
        return 'smtp.gmail.com'
    elif serviseprovider == 'outlook' or serviseprovider == 'hotmail':
        return 'smtp-mail.outlook.com'
    elif serviseprovider == 'yahoo':
        return 'smtp-mail.yahoo.com'
print("Welcome You to send email through this program")
print("Please provide Your Password and E-mail Id : ")
e_mail , serviceProvider = get_mail()
password = input("Your Password : ")

while True:
        try:
            smtpDomain = set_smtp_domain(serviceProvider)
            connect = smtplib.SMTP(smtpDomain,587)
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
                    #failure part
                    print("We can't open webpage without your Grant you can refer here https://myaccount.google.com/lesssecureapps")
                    print("Please retype your password also :")
                    e_mail , serviceProvider = get_mail()
                    password = input("The Password is : ")
                    continue
            else:
                print("Please Re-type your Correct Password :")
                e_mail, serviceProvider = get_mail()
                password = input("Password : ")
                continue
        else:
            print("Login was Successful")
            break

print("Please Provide the Receiver's Email Address too : ")
receiverAddress , receiverSP = get_mail()
print("Now please Write about the Subject And Message")
Subject = input("Subject is: ")
Message = input("Message is : ")
connect.sendmail(e_mail, receiverAddress,Subject,"\n\n",Message)
print("Email Was sent Successfully! ")
connect.quit()
