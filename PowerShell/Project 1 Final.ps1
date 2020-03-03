#This is a script to send an email reporting on hard drive space

#INSTRUCTIONS:
#To run this script, please insert your email where it reads "youremail@email.com".
#Make sure you have a gmail account inorder to authenticate to send the email.

#A function that returns information about hard drive space
function getHDSPace{
Get-PSDrive | Where {$_.Free -gt 0}
}

#Set Space Variable
$Space=getHDSpace

#What will be put in body of email
$Body= "This is how much Disk Space is on your machine."

#Exports information from above function as CSV
$Space | Export-Csv C:\HDD_Space.csv 

#Send email to user with above exported attachment
Send-MailMessage -To "youremail@email.com" -From "me@mail.com" -Subject "IT3038C WinSrv Disk Space" -Body $Body -Attachments C:\HDD_Space.csv -SmtpServer smtp.gmail.com -Port 587 -UseSsl -Credential (Get-Credential) 