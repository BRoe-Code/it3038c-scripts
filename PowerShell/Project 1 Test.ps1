#This a script to find how much hard drive space is availble on the machine, then save as a csv and email the file.

function getHDSpace{
Get-PSDrive C | Select-Object @{ E={$_.Used/1GB}; L='UsedGB' }, @{ E={$_.Free/1GB}; L='FreeGB' }
}

$Space=getHDSpace

Write-Host($Space)