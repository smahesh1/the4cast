"""
Routes and views for the flask application.
"""

"""
Use this command in kudu to update stuff
D:\home\site\wwwroot\env\Scripts>python.exe -m pip install --upgrade -r D:\home\site\wwwroot\requirements.txt 

"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
import sys
sys.path.append("c:/python")
import requests
import twilio
from twilio.rest import TwilioRestClient 

# put your own credentials here 
ACCOUNT_SID = "ACe6dfc70070586ef00b1c5a39c6040522" 
AUTH_TOKEN = "2f49cbdc4d91e523accf22158ca269d2" 

@app.route('/')
@app.route('/home', methods=["POST"])
def home():
    # This uses the REST API to send an http request
    #resp = requests.post("https://api.twilio.com/2010-04-01/Accounts/ACe6dfc70070586ef00b1c5a39c6040522/Messages.json", data={"To":"+19707655549","From":"+19709646126","Body":"Hi!"},auth=("ACe6dfc70070586ef00b1c5a39c6040522","2f49cbdc4d91e523accf22158ca269d2"))
    
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
    client.messages.create(
        to="+19707655549", 
        from_="+19709646126", 
        body="This is the ship that made the Kessel Run in fourteen parsecs?", 
        media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg", 
    )

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
