import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import data
from flask import Flask, request, render_template, redirect

smtp_server = 'smtp.gmail.com'
smtp_port = 587

smtp_username = os.getenv("GMAIL_ADDRESS")
smtp_password = os.getenv("GMAIL_PASSWORD")

app = Flask(__name__)

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        body = request.form.get('body')
        heading = request.form.get('heading')

        for to_address in data.subscriber_email_addresses:
            msg = MIMEMultipart()
            msg['From'] = smtp_username
            msg['To'] = to_address
            msg['Subject'] = heading
            msg.attach(MIMEText(body, 'plain'))

        try:
            
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.ehlo()
            server.starttls()
            server.login(smtp_username, smtp_password)
            text = msg.as_string()
            server.sendmail(smtp_username, to_address, text)
            server.quit()
        except Exception as e:
            return str(e)
        # Add an indented block of code here if needed

        return 'Emails sent!'



    return render_template('form.html')

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form.get('email')
        if email in data.subscriber_email_addresses:
                print(data.subscriber_email_addresses)
                return "This email is already subscribed."
        else:
                data.subscriber_email_addresses.append(email)
                print(data.subscriber_email_addresses)
                return redirect('/success')
    return render_template('subscribe.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    if request.method == 'POST':
        email = request.form.get('email')
        if email in data.subscriber_email_addresses:
            data.subscriber_email_addresses.remove(email)
            return 'Unsubscription successful!'
        else:
            return 'Email not found in subscriber list.'
    return render_template('unsubscribe.html')

if __name__ == '__name__':
    app.run(debug=True)