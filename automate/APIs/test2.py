import requests

def get_weather(city, units='metric', api_key='61150bc0c984493cbc95da930645443c'):
    url = f'http://api.openweather.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}'
    r = requests.get(url)
    content = r.json()
    with open('data.txt', 'a') as file:
        for dicty in content['list']:
            #print(dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['description'])
            file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")
    return content

print(get_weather(ciy="Washington'))
