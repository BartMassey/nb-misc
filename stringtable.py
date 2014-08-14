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
    from random import randrange

    def test(n):

        def randstring():
            r = ""
            for _ in range(randrange(5)):
                r += chr(randrange(32, 128))
            return r

        t = StringTable()
        entries = {}        
        for _ in range(n):
            k = randstring()
            v = randrange(1000)
            t.insert(k, v)
            entries[k] = v
        for k in entries:
            assert entries[k] == t.lookup(k)
        for _ in range(n):
            k = randstring()
            if k in entries:
                continue
            assert t.lookup(k) == None
        print(".", end="")

    print("random testing")
    for _ in range(10):
        test(64000)
