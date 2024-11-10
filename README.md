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
        Frame, { # Parent Widget
            "Create Account": (Button, 
                               {
                                   "bg": "#f00"}, 
                               {
                                   "row": 0, 
                                   "column": 0}), # Child Widget - "Widget Name": Widget type, widget_options, grid_options
            "Exit Application": (Button, 
                                 {
                                     "bg": "#00f",
                                     "command": myapp.destroy}, 
                                 {
                                     "row": 1, 
                                     "column": 0}) # Child Widget - "Widget Name": Widget type, widget_options, grid_options
            })
)

myapp()
```
