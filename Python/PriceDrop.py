import requests, re
from bs4 import BeautifulSoup

try:
    data = requests.get("https://www.amazon.com/dp/B081FZV45H").content
    soup = BeautifulSoup(data, 'html.parser')
    span = soup.find("span", {"class":"a-size-large"})
    title = span.text
    span = soup.find("span", {"class":"a-size-medium a-color-price priceBlockBuyingPriceString"})
    price = span.text
    print("Item name %s has price %s" % (title, price))
except:
    span = soup.find("an error occured")