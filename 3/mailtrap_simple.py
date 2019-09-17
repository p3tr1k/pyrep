#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText

sender = 'admin@example.com'
receiver = 'info@example.com'

msg = MIMEText('This is test mail 2')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

user = '9234a53cb553a1'
password = 'ac5082d4f4fe09'

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:

    server.login(user, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("mail successfully sent")

print(msg)