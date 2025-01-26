import yagmail
import os

sender = 'app7flask@gmail.com'
#dropmail.me
receiver = '2jjnkjca@10mail.tk'

subject = "This is the subject"

contents = '''
Here is the content of the email!
'''

#replit => secrets(environment variables) => key = PASSWORD, value = 
# manage google account => scurity -> 2-step verification -> app passwords -> others -> python automation
yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Send!")
