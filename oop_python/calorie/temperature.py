from selectorlib import Extractor
import requests

class Temperature:
    """
    Represent a temperature value extracted from the timeanddate.com/weather webpage.
    
    A scraper that uses an yml file to read the xpath of a value it needs to extract
    from the timeanddate.com/weather url

    Inspect Element
    Show Page Source

    import requests
    r = requests.get('https://www.timeanddate.com/weather/usa/san-francisco', headers=h)
    type(r)
    r

    h = { 'pragma' : 'no-cache',
          'cache-control': 'no-cache',
          'dnt': '1',
          'upgrade-insecure-requests': '1',
          'user-agent': 'Mozila/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

    c = r.content // byte (pdf, picture, files)
    from pprint import pprint
    pprint(c)

    c = r.text // string
    install selectorlib package
    from selectorlib import Extractor
    extractor = Extractor.from_yaml_file('temperature.yaml')
    add //*[@id="qlook"]/div[3] to temperature.yaml
    => /html/body/div[5]/main/article/section[1]/div[1]/div[3]

    extractor
    extractor.extract(c)
    raw_result = extractor.extract(c)
    result = float(raw_result['temp'].replace("\a@oC", ""))
    """

    h = { 'pragma' : 'no-cache',
          'cache-control': 'no-cache',
          'dnt': '1',
          'upgrade-insecure-requests': '1',
          'user-agent': 'Mozila/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'



    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        """Builds the url string adding country and city"""
        url = self.base_url + self.country + "/" + self.city
        return url

    def _scrape(self):
        """Extracts a value as instructred by the yml file and returns a dictionary"""

        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers=self.h)
        full_content= r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        """Cleans the output of _scrape"""

        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace("oC", "").strip())


if __name__ == "__main__":
    temperature = Temperature(city="rome", country='italy')
    print(temperature.get())

"""
"13 ".strip()
"""
