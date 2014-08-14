# Copyright © 2014 Bart Massey
# StringTable class as a hash table.

from djb2 import djb2

class StringTable(object):
    def __init__(self):
        self.table = []
        for _ in range(65536):
            self.table += [[]]

    # Return the value at position k.
    def lookup(self, k):
        for kv in self.table[djb2(k)]:
            (ck, cv) = kv
            if ck == k:
                return cv
        return None

    # Insert the value v at position k,
    # overwriting any existing value at k.
    def insert(self, k, v):
        h = djb2(k)
        for i in range(len(self.table[h])):
            (ck, _) = self.table[h][i]
            if ck == k:
                self.table[h][i] = (k, v)
                return
        self.table[h] += [(k, v)]

if __name__ == "__main__":
    from stringtabletest import stringtabletest

    stringtabletest(StringTable)
