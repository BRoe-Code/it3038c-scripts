import datetime

print("Please enter your birthday ")
bday_Y=int(input("Year:"))
bday_M=int(input("Month (1-12):"))
bday_D=int(input("Day:"))

date = datetime.date.today()
birthday = datetime.date(bday_Y, bday_M, bday_D)
diff = birthday - date
year = diff.days
month = -year

seconds = 86400

timeAlive = month * seconds
print ("Your age is", timeAlive, "seconds")