import json
import requests

r = requests.get('http://localhost:3000/')
data = r.json()

print(data[0]['name'], end = ' ')
print("is", end = ' ')
print(data[0]['color'])
print()
print

print(data[1]['name'], end = ' ')
print("is", end = ' ')
print(data[1]['color'])
print()
print

print(data[2]['name'], end = ' ')
print("is", end = ' ')
print(data[2]['color'])
print()
print