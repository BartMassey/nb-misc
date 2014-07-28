# Copyright © 2014 Bart Massey
# Display a die roll

from random import *
from tkinter import *

class DieRoller(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.grid()
        self.display = Label(self, width = 1)
        self.display.grid(row = 0, column = 0, sticky = E + W)
        self.roll = Button(self, text = "Roll", command = self.do_roll)
        self.roll.grid(row = 1, column = 0, sticky = E + W)
        
    def do_roll(self):
        roll = randrange(6) + 1
        self.display.configure(text = str(roll))

# Seed the PRNG.
seed()

# Start the app.
root = Tk()
root.title("Die Roller")
_ = DieRoller(root)
root.mainloop()
