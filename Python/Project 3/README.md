# What this does
This script will email you if the price of the item is below the price you set inside the script. This script can be set on a schedule so it sends the email once a day. This script is written to be manually run.

# Code to Replace
This is code you need to change inorder for the script to work.

```python
#In line 7 and 9 replace the:
'www.microcenter.com...' 
#with a website of your choosing

#In Line 8,17,28,36,and 41 make these variables equal to the ones you use in the check_price func.
#Example code:
global converted_price
converted_price = saleprice[0:6]


#Replace line 15,21,32 and 40 with the element specific to your website
#Example code:
span = soup.find("span", {"class":"ProductLink_616952"})
#To learn how to find an element see the element section below

#Line 45, replace the "2900" with a value of your choosing
#This value will make it so you are only alerted when the price is below that number
#Example code
if(float_price < 2900):

#Line 60, insert your credentials for your gmail and your google app password
#Example code:
server.login('example@gmail.com', 'googleapppassword')
#To set up a google app password see the google app password section

#Replace line 73 with the email you want to send the message from
#Replace line 74 with the email you want to send the message to
#Example Code:
        'example@gmail.com',
        'example@yahoo.com',

```

# How to Inspect an Element on a Webpage
Once you're on the webpage you want to scrape go to an element you want and right click, see example below:
![alt text](https://github.com/BRoe-Code/it3038c-scripts/blob/master/Python/Project%203/Inspect%20Element%20Step%201.png "Logo Title Text 1")



After you have clicked "inspect element" a box will appear and the code you want is highlighted, see example below:
![alt text](https://github.com/BRoe-Code/it3038c-scripts/blob/master/Python/Project%203/Inspect%20Element%20Step%202.png "Logo Title Text 1")

# How to Setup the Google App Password
To setup the Google App Password, go to myaccount.google.com and then follow the steps below:
![alt text](https://github.com/BRoe-Code/it3038c-scripts/blob/master/Python/Project%203/App%20Password%20Step%201.png "Logo Title Text 1")

Select the app and device you want to use, see example below:
![alt text](https://github.com/BRoe-Code/it3038c-scripts/blob/master/Python/Project%203/App%20Password%20Step%202.png "Logo Title Text 1")

After selecting both of those items a screen similar to the one below will pop up (Use this PW in Line 60):
![alt text](https://github.com/BRoe-Code/it3038c-scripts/blob/master/Python/Project%203/App%20Password%20Step%203.png "Logo Title Text 1")

# How to Run the Program and the Expected Output
Open PowerShell and type the command below replacing ```C:\Example\PriceDropAlert.py``` with your file path

```powershell

PS C:\> python C:\Example\PriceDropAlert.py

````

The output should look like the image below:
![alt text](https://github.com/BRoe-Code/it3038c-scripts/blob/master/Python/Project%203/Project%203%20Output.png "Logo Title Text 1")
