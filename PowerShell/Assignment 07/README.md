

# Lab 7
For this Lab I decided to use the Powershell Module Carbon. 

Carbon is used for automating a variety of things such as Windows apps, websites and Services

## Install
Let me show you how to install it.
```Powershell
PS C:\> Install-Module -Name Carbon
```
## Features
Now, say you want to create a new directory to hold some files using Powershell.
Just run the following code!
```Powershell
PS C:\> Install-Directory C:\Path\To\Directory
```

The syntax above will create a new directory.
Now we can run a simple command to revoke the access to the directory for a certain group.

```Powershell
PS C:\> Revoke-Permission -Identity DOMAIN\Group -Path 'C:\Path\To\Directory'
```

Finally, if we want to zip that directory and send it, we can do so by running...

```Powershell
PS C:\> Compress-Item -Path 'C:\Path\To\Directory' -OutFile 'C:\Directory.zip'
```
