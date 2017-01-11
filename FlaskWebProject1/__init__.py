"""
The flask application package.
"""

from flask import Flask
from twilio import twiml
app = Flask(__name__)

import FlaskWebProject1.views
