import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=45013,us&appid=5a62c781f1151f03199ae717f9578908')
data=r.json()
print (data['weather'][0]['description'])