from email.message import EmailMessage
from decouple import config
import ssl
import smtplib

"""To execute this app you need to create an .env file in main's folder and 
set inside email_sender, email_password, email_receiver variables.
The email_password is not the same that your gmail-login. You have to
go inside gmail-account's settings and get email-token.
To make test probably you gonna need a test-email. Go to https://temp-mail.org/ and get one."""

email_sender = config('email_sender')
email_password = config('email_password')
email_receiver = config('email_receiver')

subject = "Python Email Sender"

body = """
Hi there! How are you?"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context= context) as smtp:
    try:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver, em.as_string())
    except:
        print("Something goes wrong. Try Again.")
    else:
        print("Mail has been sended.")