# Balanced Search Tree
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

class SearchTree(object):
    def __init__(self, label, left, right):
        self.label = label
        self.left = left
        self.right = right
        self.n_nodes = 1 + self.nodes(left) + self.nodes(right)
        

    def nodes(self, t):
        if t == None:
            return 0
        return t.n_nodes

    def search(self, v):
        if self.label == v:
            return self
        if v < self.label and self.left != None:
            return self.left.search(v)
        if self.right != None:
            return self.right.search(v)
        return None

    def insert(self, v):
        if self.label == v:
            return
        if v < self.label:
            if self.left == None:
                t = SearchTree(v, None, None)
            else:
                self.left.insert(v)
                t = self.left.maybe_rotate_right()
            self.left = t
        else:
            if self.right == None:
                t = SearchTree(v, None, None)
            else:
                self.right.insert(v)
                t = self.right.maybe_rotate_left()
            self.right = t
        self.n_nodes = self.nodes(self.left) + self.nodes(self.right) + 1
        return

    def maybe_rotate_right(self):
        if self.nodes(self.left) <= self.nodes(self.right) + 1:
            return self
        a = self
        b = self.left
        c = self.left.right
        na = a.n_nodes - b.n_nodes + self.nodes(c)
        nb = b.n_nodes - self.nodes(c) + na
        b.right = a
        a.left = c
        a.n_nodes = na
        b.n_nodes = nb
        return b

    def maybe_rotate_left(self):
        if self.nodes(self.right) <= self.nodes(self.left) + 1:
            return self
        a = self
        b = self.right
        c = self.right.left
        na = a.n_nodes - b.n_nodes + self.nodes(c)
        nb = b.n_nodes - self.nodes(c) + na
        b.left = a
        a.right = c
        a.n_nodes = na
        b.n_nodes = nb
        return b

    def labels(self):
        vs = {self.label}
        if self.left != None:
            vs |= self.left.labels()
        if self.right != None:
            vs |= self.right.labels()
        return vs

    def depth(self):
        d = 1
        if self.left != None:
            d = max(d, 1 + self.left.depth())
        if self.right != None:
            d = max(d, 1 + self.right.depth())
        return d

    def check_nodes(self):
        n = 1
        if self.left != None:
            n += self.left.check_nodes()
        if self.right != None:
            n += self.right.check_nodes()
        assert n == self.n_nodes
        return n

    def desc(self):

        def maybe(t):
            if t == None:
                return "-"
            else:
                return t.desc()

        return str(self.label) + \
            "(" + maybe(self.left) + "," + maybe(self.right) + ")"

if __name__ == "__main__":

    from math import log2
    from random import randrange

    def test():
        # print("building tree")
        v = randrange(100)
        # print(v)
        labels = {v}
        t = SearchTree(v, None, None)
        n = randrange(1000)
        for _ in range(n):
            v = randrange(1000)
            # print(v)
            labels |= {v}
            t.insert(v)
        # print("printing tree")
        # print("n=" + str(n + 1), "depth=" + str(t.depth()))
        # print(t.desc())
        # print("checking node counts")
        t.check_nodes()
        # print("checking labels")
        assert labels == t.labels()
        # print("checking presence")
        for l in labels:
            assert t.search(l) != None
        # print("checking absence")
        for l in set(range(100)) - t.labels():
            assert t.search(l) == None
        # print("checking depth")
        depth_ok = t.depth() <= 2 * log2(t.n_nodes) + 2
        if not depth_ok:
            print(log2(t.n_nodes) + 2, t.depth())
        assert depth_ok
        print(".", end="")

    print("random tests")
    for _ in range(100):
        test()
    print()
