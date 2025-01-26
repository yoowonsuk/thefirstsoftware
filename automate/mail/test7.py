import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = 'automateeverthingwithpython@hotmail.com'
receiver 'app7flask@gmail.com'
password = 'python12345678' # password = os.getenv('PASSWORD')
# pythonhow.com : password securely

message = """\
Subject: Hello Hello

This is Ardit!
Just wanted to say hi!
"""

message = MIMEultipart() # multi-pupose internet mail extenstions
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello again!'

body = """
<h1>Hi there!</h1> # smaller h2
There are only two cats flying today!
Let's hope for more!
"""
mimetext = MIMEText(body, 'html') #'plain'
message.attach(mimetext)

attachment_path = 'tiger.jpeg'
attachment_file = open(attachment_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', filename=attachment_path)
message.attach(payload)

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
message_text = message.as_string()
#server.sendmail(sender, receiver, message) # message should be string
print(message_text)
server.sendmail(sender, receiver, message_text) # message should be string
server.quit()


