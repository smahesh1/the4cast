'''
Configuration Settings
'''

''' Uncomment to configure using the file.  
WARNING: Be careful not to post your account credentials on GitHub.

TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxx" 
TWILIO_AUTH_TOKEN = "yyyyyyyyyyyyyyyy"
TWILIO_CALLER_ID = "+17778889999"
'''

import os
TWILIO_ACCOUNT_SID = os.environ.get('ACe6dfc70070586ef00b1c5a39c6040522', None)
TWILIO_AUTH_TOKEN = os.environ.get('2f49cbdc4d91e523accf22158ca269d2', None)
TWILIO_CALLER_ID = os.environ.get('(970) 964-6126', None)
TWILIO_APP_SID = os.environ.get('MGc4ca9e0bca3533313f7cb69641f165c4', None)