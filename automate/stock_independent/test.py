from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re
import time
import requests

CHROMEDRIVER = Service('C:\\Users\\52553\\OneDrive\\Desktop\\chromedriver.exe')
driver = webdriver.Chrome(service=CHROMEDRIVER)
driver.maximize_window()
driver.get('https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6')
time.sleep(2)
change = driver.find_element(By.XPATH, '//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]').text
change = float(re.search(r'(-|\+)\d+.\d+', change).group())

if change < -.1:
    url = 'https://api.telegram.org/bot<your_bot_token>/sendMessage'
    data = {'chat_id': '<your_chat_id>', 'text': 'Stock price is down more than .10%'}
    requests.post(url, data=data)
