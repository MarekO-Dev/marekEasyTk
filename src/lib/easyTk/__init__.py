from tkinter import *
from PIL import Image, ImageTk

class Application(Tk):
    def __init__(self, **kwargs):
        super().__init__()  

        self._window_size = kwargs["window_size"]
        self.elements = []

    def __call__(self):
        '''
            On instance call: start application loop
        '''
        try:
            self.geometry(f"{self._window_size[0]}x{self._window_size[1]}")
        except Exception as err:
            print("Values must be integers", "and", ":", err)
        
        #start mainloop if all is good
        self.mainloop()

    def addElements(self, **kwargs: tuple[int, Widget, dict[Widget, ...]]):
        '''
            ### addElements(self, *args: dict)
        '''

        for element_name, element in kwargs.items():
            master = None
            if element[0] == 0 or element[0] is int:
                master = self
            else:
                master = element[0]
            parent_widget = element[1]
            children_widgets = element[2]

            pw = parent_widget(master = master)
            pw.grid(row = 0, column = 0)

            for child_name, child_object in children_widgets.items():
                self.elements.append(
                    child_object[0](pw, text = child_name,**child_object[1]).grid(**child_object[2])
                )