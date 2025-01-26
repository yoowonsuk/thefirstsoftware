import yagmail
import os
import pandas

sender = 'app7flask@gmail.com'
#dropmail.me
receiver = '2jjnkjca@10mail.tk'

subject = "This is the subject"

contents = '''
Here is the content of the email!
'''

#replit => secrets(environment variables) => key = PASSWORD, value = 
# manage google account => scurity -> 2-step verification -> app passwords -> others -> python automation

#command or ctrl slash => comment
df = pandas.read_csv('contacts.csv')
print(df)

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

for index, row in df.iterrows():
    #yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    #print(index, row['email'])

    contents = f'''
    {row['name']} Here is the content of the email!
    '''
    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email Send!")
