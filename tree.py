# Copyright © 2014 Bart Massey
# Tree class.

def tree_value(n):
    if n == None:
        return 0
    return n

class Tree(object):
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def postorder(self, op):
        l = None
        if self.left != None:
            l = self.left.postorder(op)
        r = None
        if self.right != None:
            r = self.right.postorder(op)
        return op(self.label, l, r)

    def print_inorder(self):
        if self.left != None:
            self.left.print_inorder()
        print(self.label)
        if self.right != None:
            self.right.print_inorder()

    def print_preorder(self):
        print(self.label)
        if self.left != None:
            self.left.print_preorder()
        if self.right != None:
            self.right.print_preorder()

    def print_postorder(self):
        def op(label, left, right):
            print(label)

        self.postorder(op)

    def sum(self):
        def op(label, left, right):
            return label + tree_value(left) + tree_value(right)

        return self.postorder(op)

    def nodes(self):
        def op(label, left, right):
            return 1 + tree_value(left) + tree_value(right)

        return self.postorder(op)

demo_tree = Tree(1, Tree(2, Tree(4, None, Tree(5))), Tree(3))
                                                                                                            
