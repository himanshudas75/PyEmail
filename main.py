import os
from dotenv import load_dotenv
import smtplib, ssl
import sys
from modules.clear import clean
from modules.sendmail import send

intro="""\
  _____          ______                    _  _ 
 |  __ \        |  ____|                  (_)| |
 | |__) |_   _  | |__    _ __ ___    __ _  _ | |
 |  ___/| | | | |  __|  | '_ ` _ \  / _` || || |
 | |    | |_| | | |____ | | | | | || (_| || || |
 |_|     \__, | |______||_| |_| |_| \__,_||_||_|
          __/ |                                 
         |___/                                  

Send Emails Using Python
"""
print(intro)
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
load_dotenv(f'{FILE_PATH}/env')

EMAIL=os.getenv('EMAIL')
PASSWORD=os.getenv('PASSWORD')
PORT=465

print("Authenticating...")

context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com',PORT,context=context)

try:
    server.login(EMAIL, PASSWORD)
except:
    print("Authentication Error. Please check if email and password provided in the env file are correct.\n")
    sys.exit(0)

print("Authenticated Successfully!\n")
print(f"Welcome, {EMAIL}")

menu="""\

1> Send an email now.
2> Show/Configure stored receiver email addresses.
3> Message Drafts.
4> Exit

Choose an option: """

menu1="""\

1> Receiver Email
2> Subject
3> Body
4> Attachments
5> Preview
6> Back
"""
while(True):
    print(menu)
    opt = int(input())
    if opt == 1:
        clean()

    break