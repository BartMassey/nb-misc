# Balanced Search Tree
# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

def nodes(t):
    if t == None:
        return 0
    return t.n_nodes

def depth(t):
    if t == None:
        return 0
    return t.n_depth

class SearchTree(object):
    def __init__(self, label, left, right):
        self.label = label
        self.left = left
        self.right = right
        self.n_nodes = 1 + nodes(left) + nodes(right)
        self.n_depth = 1 + max(depth(left), depth(right))
        

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
            return self
        if v < self.label:
            if self.left == None:
                self.left = SearchTree(v, None, None)
            else:
                self.left = self.left.insert(v)
            t = self.maybe_rotate_right()
        else:
            if self.right == None:
                self.right = SearchTree(v, None, None)
            else:
                self.right = self.right.insert(v)
            t = self.maybe_rotate_left()
        t.n_depth = t.implied_depth()
        t.n_nodes = t.implied_nodes()
        return t

    def maybe_rotate_left(self):
        if depth(self.right) <= depth(self.left):
            return self
        a = self
        b = self.right
        c = b.left
        a.right = c
        b.left = a
        a.n_nodes = a.implied_nodes()
        a.n_depth = a.implied_depth()
        return b

    def maybe_rotate_right(self):
        if depth(self.left) <= depth(self.right):
            return self
        a = self
        b = self.left
        c = b.right
        a.left = c
        b.right = a
        a.n_nodes = a.implied_nodes()
        a.n_depth = a.implied_depth()
        return b


    def implied_nodes(self):
        return nodes(self.left) + nodes(self.right) + 1

    def implied_depth(self):
        return max(depth(self.left), depth(self.right)) + 1

    def labels(self):
        vs = {self.label}
        if self.left != None:
            vs |= self.left.labels()
        if self.right != None:
            vs |= self.right.labels()
        return vs

    def check_nodes(self):
        n = 1
        if self.left != None:
            n += self.left.check_nodes()
        if self.right != None:
            n += self.right.check_nodes()
        assert n == self.n_nodes
        return n

    def check_balance(self):
        if self.left != None:
            self.left.check_balance()
        if self.right != None:
            self.right.check_balance()
        assert self.n_depth == self.implied_depth()
        assert abs(depth(self.left) - depth(self.right)) <= 1

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
        nr = 50
        print("building tree")
        v = randrange(nr)
        print(v)
        labels = {v}
        t = SearchTree(v, None, None)
        t.check_nodes()
        n = randrange(nr) + 1
        while len(labels) < n:
            v = randrange(nr)
            if v in labels:
                continue
            # print(v)
            labels |= {v}
            t = t.insert(v)
        print("printing tree")
        print("n=" + str(n), "depth=" + str(t.n_depth))
        print(t.desc())
        print("checking tree size")
        assert n == nodes(t)
        print("checking node counts")
        t.check_nodes()
        print("checking labels")
        assert labels == t.labels()
        print("checking presence")
        for l in labels:
            assert t.search(l) != None
        print("checking absence")
        for l in set(range(100)) - t.labels():
            assert t.search(l) == None
        print("checking balance")
        t.check_balance()
        print(".", end="")
        print("checking depth")
        assert t.n_depth <= log2(t.n_depth) + 1


    print("random tests")
    for _ in range(10):
        test()
    print()
