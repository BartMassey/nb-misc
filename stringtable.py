# Copyright © 2014 Bart Massey
# StringTable class as a hash table.

from djb2 import djb2

class StringTable(object):
    def __init__(self):
        self.table = [[]]*65536

    # Return the value at position k.
    def lookup(self, k):
        return None

    # Insert the value v at position k,
    # overwriting any existing value at k.
    def insert(self, k, v):
        pass

if __name__ == "__main__":
    from stringtabletest import stringtabletest

    stringtabletest(StringTable)
