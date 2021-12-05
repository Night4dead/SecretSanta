from email.mime import multipart
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

test_msg = """\
    Subject: test mail
    
    this message is sent from python"""

def configserver(login,password):
    smtp_server = "smtp.gmail.com"
    port = 587 #for starttls
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    #create security context
    context = ssl.create_default_context()
    #secures the server and logins
    server.starttls(context=context)
    server.ehlo()
    server.login(login,password)
    #returns the server
    return server

def createmessage(sender,dest,message,subject):
    print("creating mail ...")
    #creates the mail header
    multi = MIMEMultipart("alternative")
    multi["Subject"]=subject
    multi["From"]=sender
    multi["To"]=dest
    #creates the mail body
    msg = MIMEText(message,"plain")
    #attaches the mail body to the header
    multi.attach(msg)
    #returns final mail body
    return multi.as_string()

def sendmail(sender,dest,message,subject,server):
    message = createmessage(sender,dest,message,subject)
    print("sending mail...")
    server.sendmail(sender,dest,message)

def usemail(server,sender,dest,message,subject):
    try:
        sendmail(sender,dest,message,subject,server)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("smtp mail server for sending mails")
    usemail("pyth0n.s3cretsanta+recv@gmail.com",test_msg,"secret santa test")