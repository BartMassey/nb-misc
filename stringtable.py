# Copyright © 2014 Bart Massey
# StringTable class as a hash table.

from djb2 import djb2

def StringTable(object):
    def __init__(self):
        self.table = [None]*65536

    def lookup(self, k):
        pass

    def insert(self, k, v):
        pass
