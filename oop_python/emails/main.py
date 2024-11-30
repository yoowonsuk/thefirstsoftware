import requests
from pprint import pprint

class NewsFeed:
    """Representing multiple news titles and links as a single string
    """
    base_url = "http://newsapi.org/v2/everything?"
    api_key = "47d2c0b06bc7454d904934f9349561ce"

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        #url = "https://newsapi.org/v2/everything?" \
        #url = f"{self.base_url}?" \
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"sortBy=publishedAt&" \
              f"language={self.language}&" \
              f"apiKey=47d2c0b06bc7454d904934f9349561ce"

        response = requests.get(url)
        content = response.json()
        pprint(content)
        articles = content['articles']

        email_body = ''
        for article in articles: #resume
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n' # break line

        return email_body


news_feed = NewsFeed(interest='nasa', from_date='2024-11-12', to_date='2024-11-13', language='en')
print(news_feed.get())


"""
# q=meditation
# qInTitle
# records on 13th October 2020
# backslash \
# "http://blahblah" \
# "q=meditation&" \
# "apiKey=blahblah"
response = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2024-10-22&sortBy=publishedAt&apiKey=47d2c0b06bc7454d904934f9349561ce")
#content = response.text
content = response.json()
x = content['articles'][2]['title'] #third article
#content['articles'][2]['url']
pprint(content)

articles = content['articles']

email_body = ''
for article in articles: #resume
    email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n' # break line
    print(article['title'], article['url'])

print(email_body)
"""
