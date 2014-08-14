# Copyright © 2014 Bart Massey
# StringTable class tests


from random import randrange

def stringtabletest(constructor):

    def test(n):

        def randstring():
            r = ""
            for _ in range(randrange(5)):
                r += chr(randrange(32, 128))
            return r

        t = constructor()
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
