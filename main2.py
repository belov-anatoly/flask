import requests
from datetime import datetime

town = input('Введите город: ')

key = 'a55fd0196b4eb669cacc8ff27e977bda'
url = 'http://api.openweathermap.org/data/2.5/weather'
params = {'APPID': key, 'q': 'Санкт Петербург', 'units': 'metric'}

request = requests.get(url, params=params)

result = request.json()
# print(result)
code = result['cod']

if code != '401':
    if code != '404':
        data = result['main']
        print(f'Температура: {data["temp"]:.1f}\xB0C')
        print('Влажность', data['humidity'], '%')
        raw_time_sunset = result['sys']['sunset']
        print(datetime.utcfromtimestamp(raw_time_sunset).strftime("%H:%M"))
        print(f'Координаты: {result["coord"]["lon"]}, {result["coord"]["lat"]}')
        if result['weather'][0]['main'] == 'Clouds':
            print('Облачно')
else:
    print('Информации нет!')
