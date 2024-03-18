import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import data

smtp_server = 'smtp.gmail.com'
smtp_port = 587

smtp_username = os.getenv("GMAIL_ADDRESS")
smtp_password = os.getenv("GMAIL_PASSWORD")

# Define your email settings
from_address = smtp_username
subject = 'Your Email Subject'
body = 'Your email body goes here.'

# Connect to the server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Loop over the email addresses
    for to_address in data.subscriber_email_addresses:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.send_message(msg)

print('Emails sent successfully.')