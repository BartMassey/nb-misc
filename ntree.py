# Copyright © 2014 Bart Massey
# N-ary trees.

class NTree(object):
    def __init__(self, label, children):
        self.label = label
        self.children = children
        
    def str(self):
        if self.children == []:
            return str(self.label)
        result = str(self.label) + "("
        substrs = []
        for c in self.children:
            substrs += [c.str()]
        result += substrs.sep(",")
        result += ")"
        return result
        
        
