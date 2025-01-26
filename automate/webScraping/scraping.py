from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service('C:\\Users\\arditsulce\\Downloads\\chromedriver.exe')
# MAC /Users/arditsulce/Downloads/chromedriver

def get_driver():
  # Set options to make browsing easier
  # https://wikidocs.net/177133
  options = webdriver.ChromeOptions()
  options.add_argument('disable-infobars')
  options.add_argument('start-maximized')
  options.add_argument('disable-dev-shm-usage') # for Linux
  options.add_argument('no-sandbox')
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  #driver = webdriver.Chrome(options, service=service)
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output
  

def main():
  driver = get_driver()
  #element = driver.find_element_by_xpath(by="xpath", value="/html/body/div[1]/div/h1[1]")
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
  # /div ?? or google chrome copy full xpath
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  #return element.text
  return clean_text(element.text)

print(main())