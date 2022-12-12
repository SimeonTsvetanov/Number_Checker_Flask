from flask import Flask, render_template, request, flash, session

# imports for the number tracking library
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

app = Flask(__name__)
app.secret_key = "password"


@app.route('/')
def index():
    flash("")
    return render_template('index.html')


@app.route("/check", methods=['GET', 'POST'])
def check():
    number = str(request.form['number_input'])

    # Parse the number to phonenumbers library:
    ch_number = phonenumbers.parse(number, "CH")

    # Get the country and server provider:
    country = geocoder.description_for_number(ch_number, "en")
    server_provider = carrier.name_for_number(phonenumbers.parse(number, "RO"), "en")

    flash(f"The number: {number} is from {country}, and it's using the Service Provider: {server_provider}")
    return render_template('index.html')
