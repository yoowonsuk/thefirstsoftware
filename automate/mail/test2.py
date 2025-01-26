# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import yagmail
import os
import time
from datetime import datetime as dt

sender = 'app7flask@gmail.com'
receiver = '2jjnkjca@10mail.tk'

subject = """
This is the subject!
"""
contents = """
Here is the content of the email! 
Hi!
"""
while True:
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(60)

while True:
    now = dt.now()
    if now.hour == 13 and now.minute == 15:
        yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD')) # Secrets: PASSWORD / flask7app#
        yag.send(to=receiver, subject=subject, contents=contents)
        print("Email Sent!")
        time.sleep(60)
    
# pythonanywhere : Another way to execute a script at a specific time every day is by uploading your script to PythonAnywhere and telling PythonAnywhere the time when to run the script:
# https://pythonhow.com/how/schedule-a-python-script-for-execution-at-a-specific-time-every-day/
