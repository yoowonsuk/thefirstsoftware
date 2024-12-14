import requests, pprint

url = "http://api.openweathermap.org/data/2.5/forcast?q=Madrid&APPID=26631f0f41b95fb9f5ac0df9a8f43c92&units=imperial"
#url = "http://api.openweathermap.org/data/2.5/forcast?lat=40.1&lon=3.4&APPID=26631f0f41b95fb9f5ac0df9a8f43c92&units=imperial"
r = requests.get(url)
print(r)
print(r.text)
print(type(r.test)) # str

print(type(r.json()) # dict

class Weather:
    """"Creates a Weather object getting an api key as input
    and either a city name or lat and lon coordinates.

    Package use example:

    # Create a weather object using a city name:
    # The api key below is not guranateed to work.
    # Get your own apikey from https://openweathermap.org
    # And wait a couple of hours for the apikey to be activated

    >>> weather1 = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", city = "Madrid")

    # Using latitute and logitude coordinates
    >>> weather2 = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", lat = 41.1, lon =-4.1)

    # Get complete weather data for the next 12 hours:
    >>> weather1.next_12h()

    # Simplified data for the next 12 hours:
    >>> weather1.next12h_simplified()

    Sample url to get sky condition icons:
    http://openweathermap.org/img/wn/10d@2x.png

    """
    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"http://api.openweathermap.org/data/2.5/forcast?q={city}&APPID={apikey}&units=imperial"
            r = requests.get()
            self.data = r.json()
        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forcast?lat={lat}&lon={lon}&APPID={apikey}&units=imperial"
            r = requests.get()
            self.data = r.json()
        else:
            print("Provide either a city or lat and lon arguments")
            raise TypeError("provide either a city or late and lon arguments") # dir(__buildins__) help(TypeError)
            # docs.python.org/3/library/index.html => Built-in Exceptions

        if self.data["cod"] != "200":
            raise ValueError(self.data["message"])


    def next_12h(self):
        """Returns 3-hour data for the next 12 hours as a dict.
        """
        print(self.data)
        #return self.data
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """Returns date, temperature, and sky condition every 3 hours
           for the next 12 hours as a tuple of tuples.
        """
        simpe_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append(dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['desciption'], dicty['weather'[0]['icon'])
        return simple_data
        #return (self.data['list'][0]['dt_txt'], self.data['list'][0]['main']['temp'], self.data['list'[0]['weather'][0]['description'])


city = "Rome"
apikey = "26631f0f41b95fb9f5ac0df9a8f43c92"
f"http://api.openweathermap.org/data/2.5/forcast?q={city}&APPID={apikey}&units=imperial"

weather = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", city = "Valencia")
print(weather.data)
pprint.print(weather.next_12h())


from sunnyday import Weather
weather = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", city = "Madrid")


weather1.next_12h_simplified()[0][-1]
