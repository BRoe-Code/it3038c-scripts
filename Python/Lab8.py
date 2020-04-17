import requests, re
from bs4 import BeautifulSoup

try:
    data = requests.get("https://alphaleteathletics.com/collections/black-friday-all-mens/products/tactical-hoodie-smokeblue").content
    soup = BeautifulSoup(data, 'html.parser')
    span = soup.find("h1", {"class":"product-single__title new-product-title"})
    title = span.text
    span = soup.find("span", {"class":"product__price new-price"})
    price = span.text
    span = soup.find("h1", {"class":"new-product-color"})
    color = span.text
    span = soup.find("select", {"class":"product-single__variants"})
    size = span.text
    print("Item name %s has price %s is %s color and is avaiable in %s sizes" % (title, price, color, size))
except:
    span = soup.find("an error occured")