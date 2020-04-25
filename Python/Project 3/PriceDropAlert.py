import requests, re
from bs4 import BeautifulSoup
import smtplib

def check_price():
    #The webpage soup will be searching
    data = requests.get('https://www.microcenter.com/product/616952/apple-macbook-pro-with-touch-bar-mvvk2ll-a-2019-16-laptop-computer---space-gray').content
    global url
    url = 'https://www.microcenter.com/product/616952/apple-macbook-pro-with-touch-bar-mvvk2ll-a-2019-16-laptop-computer---space-gray'

    #Parses data on the page so we can pull individual elements
    soup = BeautifulSoup(data, 'html.parser')

    #The element soup is searching the webpage for and coverting to text and shortining output
    span = soup.find("span", {"class":"ProductLink_616952"})
    title = span.text
    global converted_title 
    converted_title = title[0:67]

    #The element soup is searching the webpage for and converting to text
    span = soup.find("span", {"id":"pricing"})
    saleprice = span.text

    #Sale Price in float format for if statement
    float_price = float(saleprice[1:6].replace(',',''))

    #Sale Price in standard format with $
    global converted_price
    converted_price = saleprice[0:6]

    #The element soup is searching the webpage for and converting to text
    span = soup.find("div", {"class":"savings"})
    origprice = span.text

    #Original product price in standard format
    global converted_origprice
    converted_origprice = origprice[0:6]

    #The element soup is searching the webpage for and converting to text
    span = soup.find("span", {"class":"inventoryCnt"})
    global inv
    inv = span.text
    
    #This is used for if the price is lower than the set number "2900" it will send the email
    if(float_price < 2900):
        send_mail()

    #This shows the contents of the email being sent 
    print("The %s at Microcenter is on sale for %s with a normal price of %s and they have %s. View more details at: %s" % (converted_title, converted_price, converted_origprice, inv, url))


def send_mail():
    #This is used to determine the mail server you are sending from and what port
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    #Server Login Credentials both email and password
    server.login('example@gmail.com', 'googleapppassword')
    
    #Subject of email
    subject = 'Price Drop Alert!'
    
    #Body of email
    body = "The %s at Microcenter is on sale for %s with a normal price of %s and they have %s. View more details at: %s" % (converted_title, converted_price, converted_origprice, inv, url)
    
    #Formatting for email
    msg = f"Subject: {subject}\n\n{body}"
    
    #The email you are sending from and what email you are sending to plus contents
    server.sendmail(
        'example@gmail.com',
        'example@yahoo.com',
        msg
    )
    
    #Confirms email has been sent
    print('Email has been sent!')
    
    #Cancels connection to server
    server.quit()

#Calls the check_price function
check_price()