"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect
import twilio.twiml
from FlaskWebProject1 import app


@app.route('/home')
def home():
    """Renders the home page."""
    """Respond to incoming calls with a simple text message."""

    

    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
    
@app.route('/', methods=['GET', 'POST'])
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Renders the contact page."""

    resp = twilio.twiml.Response()
    resp.message("Hello, World!")

    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.',
        response = str(resp)
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
