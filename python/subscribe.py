from flask import Flask, request, render_template, redirect
import data

app = Flask(__name__)

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form.get('email')
        if email:  # Add any necessary validation here
            if email in data.subscriber_email_addresses:
                return "This email is already subscribed."
            else:
                data.subscriber_email_addresses.append(email)
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

if __name__ == '__main__':
    app.run(debug=True)