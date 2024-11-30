import yagmail
import pandas
import news import NewsFeed
import datetime

#df = pandas.DataFrame([1,2, 'a'])
#df
#df = pandas.DataFrame([[1, 2, 'a'], [3, 4, 'b'], [5, 6, 'c']])
#df

df = pandas.read_excel('people.xlsx')
print(df) #xlrd install package

for index, row in df.iterrows():
    #print(row)
    #print(rowi['email'])

    #news_feed = NewsFeed(interest=row['interest'], from_date='2020-11-14', to_date='2020-11-15', language='en')
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1).strftime('%y-%m-%d')

    news_feed = NewsFeed(interest=row['interest'], from_date=yesterday, to_date=datetime.datetime.now().strftime('%Y-%m-%d'), language='en')
    email = yagmail.SMTP(user="pythoncourse1@gmail.com", password="python_pro_course_1")
    email.send(to=row['email'], subject=f"Your {row['interest']} news for today!",
            contents="Hi {row['name']}\n See what's on about {row['interest']} today. \n{news_feed.get()}\nArdit")  # ctrl _ P to see what other methods we can prass there

#ctrl + / => block comment
email = yagmail.SMTP(user="pythoncourse1@gmail.com", password="python_pro_course_1")
email.send(to="", subject="Hi there!", contents="Hi, this is the body of the email!\nArdit",attachments="design.txt")  # ctrl _ P to see what other methods we can prass there

# do not name email.py (circular import) => Refactor
# manage your google account => Security => signing in to Google => 2 step verification => app passwords => python automation

"""
import datetime
import time
while True:
    if datetime.datetime.now().hour == 17 and datetime.datetime.now().minute == 43:
        print("Executing!")
    time.sleep(60)


extract method!
