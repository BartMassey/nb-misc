# Copyright © 2014 Bart Massey
# Demo of piecewise classes.

def _hello(self):
    print("hello")

def _increment(self):
    self.x = self.x + 1
    print(self.x)

class Piecewise(object):
    def __init__(self):
        self.x = 0

    hello = _hello

    increment = _increment
