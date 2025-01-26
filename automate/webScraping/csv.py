import requests
from datetime import datetime
import time

ticker = input("Enter the ticker symbol: ")
from_date = input('Enter start date in yyyy/mm/dd format:')
to_date = input('Enter end date in yyyy/mm/dd format:')

d = datetime.strptime(from_date, '%Y/%m/%d')
from_epoch = int(time.mktime(d.timetuple()))

d = datetime.strptime(from_date, '%Y/%m/%d')
to_epoch = int(time.mktime(d.timetuple()))

#url = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period=345427200&period2=1642032000&interval=1d&events=history&includeAdjustedClose=true"
url = "https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url, headers=headers).content
print(content)

with open('data.csv', 'wb') as file: # .content => wb else => w
    file.write(content)
