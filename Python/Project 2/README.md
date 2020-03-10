# What this does
This script launches a seperate window where you can play the snake game. The goal of the game is to collect as much food (yellow dot) as possible without running into the walls or yourself.

# Controls for the Game
These are the controls to be used in the game:


```python

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

```

# How to Run the Program and the Expected Output
Open PowerShell and type the command below replacing ```C:\Example\Snake.py``` with your file path

```powershell

PS C:\> python C:\Example\Snake.py

````

The output should look like the image below:

![alt text](https://github.com/BRoe-Code/it3038c-scripts/blob/master/Python/Project%202/Snake%20Example.PNG "Logo Title Text 1")
