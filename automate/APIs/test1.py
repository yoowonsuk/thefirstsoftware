import requests


r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-2-27&to=2022-2-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
#r = requests.get('https://newsapi.org/v2/everything?qInTitle=united%20state&from=2022-2-27&to=2022-2-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
content = r.json()
print(type(content))
print(content['articles'][0]['title'])
#print(content['articles'][0]['description'])

'''
for article in articles:
    print(article['title'])
    '''
def get_news(topic, from_date, to_date, language='en', api_key='61150bc0c984493cbc95da930645443c'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news(topic='space', from_date='2024-11-20', to_Date'2024-12-20'))

def get_news_c(country, language='en', api_key='61150bc0c984493cbc95da930645443c'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news(country='us'))

