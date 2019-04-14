import os
import smtplib
import imghdr
from email.message import EmailMessage

# Use Linux shell command: export EMAIL_USER=xxxxxx@gmail.com
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['example1@gmail.com', 'example2@example.com']

msg = EmailMessage()
msg['Subject'] = 'Hello, just a demo.'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content('Hows going')

files = ['test.pdf']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)