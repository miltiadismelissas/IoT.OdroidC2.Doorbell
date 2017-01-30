from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

recipients = ['abc@gmail.com']
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = str(sys.argv[1])
msg['From'] = 'abc@gmail.com'
msg['Reply-to'] = 'xyz@gmail.com'
 
msg.preamble = 'Multipart massage.\n'
 
part = MIMEText("Hello! There is someone ringing your doorbell. A picture of this person has been atached.")
msg.attach(part)

part = MIMEApplication(open(str(sys.argv[2]),"rb").read())
part.add_header('Content-Disposition', 'attachment', filename=str(sys.argv[2]))
msg.attach(part)

server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login('abc@gmail.com','password')
 
server.sendmail(msg['From'], emaillist , msg.as_string())
