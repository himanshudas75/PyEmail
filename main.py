import smtplib, ssl
import os
from dotenv import load_dotenv

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
load_dotenv(f'{FILE_PATH}/env')

EMAIL=os.getenv('EMAIL')
PASSWORD=os.getenv('PASSWORD')
PORT=465

context = ssl.create_default_context()

server = smtplib.SMTP_SSL('smtp.gmail.com',PORT,context=context)

server.login(EMAIL, PASSWORD)
message='Hello\n\nThis is my message to you hoo-hoo!'

server.sendmail(EMAIL, "iwannasmmashyouup@gmail.com",message)
server.quit()