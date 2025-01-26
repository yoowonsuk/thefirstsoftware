from bs4 import BeautifulSoup #pip install beautifulsoup4
import requests # pip install requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1#google_vignette' # placeholder
    #print(url)
    content = requests.get(url).text # source code = HTML, CSS, JavaScript
    soup = BeautifulSoup(content, 'htmp.parser')
    rate = soup.find('span', class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    print(currency)
    #print(type(currency))
    return rate


get_currency('INR', 'USD')
get_currency('EUR', 'AUD')
