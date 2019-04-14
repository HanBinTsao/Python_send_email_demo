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

msg.set_content('This is a plain text mail')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)