"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
import sys
sys.path.append("c:/python")
import requests
import twilio

#import twilio

@app.route('/')
@app.route('/home', methods=["POST"])
def home():
    resp = requests.post("https://api.twilio.com/2010-04-01/Accounts/ACe6dfc70070586ef00b1c5a39c6040522/Messages.json", data={"To":"+19707655549","From":"+19709646126","Body":"Hi!"},auth=("ACe6dfc70070586ef00b1c5a39c6040522","2f49cbdc4d91e523accf22158ca269d2"))
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
