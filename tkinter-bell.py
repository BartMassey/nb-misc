# Copyright © 2014 Bart Massey
# tkinter bell demo.

from tkinter import *

class Bell(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack()
        self.button = Button(self, text = "Bell", command = self.do_bell)
        self.button.pack()

    def do_bell(self):
        root.bell()
    

# Start the app.
root = Tk()
root.title("Socrate")
app = Bell(root)
root.mainloop()
app.close()
