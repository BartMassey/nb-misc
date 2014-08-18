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

    def frontier(self):
        def maybe_traverse(t):
            if t == None:
                return []
            else:
                return t.frontier()

        if self.left == None and self.right == None:
            return [self.label]
        l = maybe_traverse(self.left)
        r = maybe_traverse(self.right)
        return l + r

    def _frontier(self):
        if self.left == None and self.right == None:
            return [self.label]
        elif self.left == None:
            return self.right._frontier()
        elif self.right == None:
            return self.left._frontier()
        else:
            return self.left._frontier() + self.right._frontier()

    def widths(self):
        def zip(left, right):
            # If one of the lists is empty, there's
            # nothing to add, so return the other one.
            if left == []:
                return right
            if right == []:
                return left
            # Return the sum of the first elements with
            # the zip of the rest tacked on.
            return [left[0] + right[0]] + zip(left[1:], right[1:])

        def _zip(left, right):
            # * start with an empty result list
            result = []
            # * as long as there's elements on both sides,
            #   tack their sum onto the result list.
            common = min(length(left), length(right))
            for i in range(common):
                result.append(left[i] + right[i])
            # * tack on whatever's left over from one of the lists
            return result + left[common:] + right[common:]
            

        if self.left == None and self.right == None:
            return [1]
        elif self.left == None:
            return [1] + self.right.widths()
        elif self.right == None:
            return [1] + self.left.widths()
        else:
            return [1] + zip(self.left.widths(), self.right.widths())

    def width(self):
        return max(self.widths())

demo_tree = Tree(1, Tree(2, Tree(4, None, Tree(5))), Tree(3))
                                                                                                            
