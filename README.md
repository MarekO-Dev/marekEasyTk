Usage:

example main.py file:

```py
from lib.mareksEasyTk import *
from tkinter import *

myapp = Application(
    window_size = (864, 600))
myapp.title("Testor")

addElements = myapp.addElements

addElements(
    buttons_container1 = (
        0, # master 
        Frame, # Parent Widget class reference
        { 
            "Create Account": (Button, # Child widget class reference
                               {"bg": "#f00"}, #Child widget options
                               {"row": 0, "column": 0}), # Child widget grid options
            "Exit Application": (Button, # Child widget class reference
                                 {"bg": "#00f", "command": myapp.destroy}, 
                                 {"row": 1, "column": 0})
        }))

myapp()
```
