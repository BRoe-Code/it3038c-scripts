#This is a script to send an email with info about our server

#a function that returns an IP address starting with 192
function getIP{
(Get-NetIPAddress).ipv4address | Select-String "192*"
}

function getUser{
    $env:USERNAME
}

function getHostname{
    $env:computername
}

function getVersion{
    $HOST.Version.Major
}

function getDate{
    Get-Date
}

#set the IP Variable
$IP=getIP

#Set User Variable
$USER=getUser

#Set Host Variable
$Host=getHostname

#Set Version Variable
$Version=getVersion

#Set Date Variable
$Date=getDate

#set the Body Variable
$Body = "This machine's IP is $IP. User is $USER. Hostname is $Host. Powershell Version $Version. Today's Date is $Date"

#build and send the email
Send-MailMessage -To "youremail@email.com" -From "me@mail.com" -Subject "IT3038C Windows SysInfo" -Body $Body -SmtpServer smtp.gmail.com -Port 587 -UseSsl -Credential (Get-Credential)

#confirm we reached the end
Write-Host("Email Sent")
