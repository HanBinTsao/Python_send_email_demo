import os
import smtplib
from email.message import EmailMessage

# Use Linux shell command: export EMAIL_USER=xxxxxx@gmail.com
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_RECEIVE_ADDRESS = os.environ.get('EMAIL_REC_ADD')

msg = EmailMessage()
msg['Subject'] = 'Hello, just a demo.'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_RECEIVE_ADDRESS
msg.set_content('Hows going')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    smtp.send_message(msg)