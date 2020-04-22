import requests, re
from bs4 import BeautifulSoup
import smtplib

def check_price():
    #The webpage soup will be searching
    data = requests.get('https://www.microcenter.com/product/616952/apple-macbook-pro-with-touch-bar-mvvk2ll-a-2019-16-laptop-computer---space-gray').content

    #Parses data on the page so we can pull individual elements
    soup = BeautifulSoup(data, 'html.parser')

    #The element soup is searching the webpage for and coverting to text and shortining output
    span = soup.find("span", {"class":"ProductLink_616952"})
    title = span.text
    converted_title = title[0:67]

    #The element soup is searching the webpage for and converting to text
    span = soup.find("span", {"id":"pricing"})
    saleprice = span.text

    #Sale Price in float format for if statement
    converted_price = float(saleprice[1:6].replace(',',''))

    #Sale Price in standard format with $
    conv_price = saleprice[0:6]

    #The element soup is searching the webpage for and converting to text
    span = soup.find("div", {"class":"savings"})
    origprice = span.text

    #Original product price in standard format
    converted_origprice = origprice[0:6]

    #The element soup is searching the webpage for and converting to text
    span = soup.find("span", {"class":"inventoryCnt"})
    inv = span.text
    if(converted_price < 2900):
        send_mail()
        print(conv_price)
#print(converted_title)

#print(converted_origprice)
    print("The %s at Microcenter is on sale for %s with a normal price of %s and they have %s." % (converted_title, conv_price, converted_origprice, inv))


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('example@gmail.com', 'googleapppassword')
    
    subject = 'Price Drop Alert!'
    
    body = print("The %s at Microcenter is on sale for %s with a normal price of %s and they have %s." % (converted_title, conv_price, converted_origprice, inv))
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'from@gmail.com',
        'to@gmail.com',
        msg
    )
    print('Email has been sent!')
    
    server.quit()
    
check_price()