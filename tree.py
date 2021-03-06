# Copyright © 2014 Bart Massey
# Tree class.

def tree_value(n):
    if n == None:
        return 0
    return n

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

    def depth(self):
        def op(label, left, right):
            return 1 + max(tree_value(left), tree_value(right))

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

    def str(self):
        def maybe_str(t):
            if t == None:
                return "-"
            return t.str()
        
        if self.left == None and self.right == None:
            return str(self.label)
        l = maybe_str(self.left)
        r = maybe_str(self.right)
        return str(self.label) + "(" + l + "," + r + ")"

    def print(self, *args, **kwargs):
        print(self.str(), *args, **kwargs)
        
    def pretty_print(self):
        def adjust(t, k):
            if t == None:
                return
            t.indent += k
            adjust(t.left, k)
            adjust(t.right, k)

        def label_indents(t):
            if t == None:
                return
            lindent = 0
            if t.left != None:
                label_indents(t.left)
                lindent = t.left.indent
            rindent = 0
            if t.right != None:
                label_indents(t.right)
                rindent = t.right.indent
            t.indent = lindent + 2 + len(str(t.label)) // 2 + rindent // 2
            adjust(t.right, t.indent)

        label_indents(self)

        def indented_labels(t, d):
            if t == None:
                return []
            if d == 1:
                return [(t.indent, t.label)]
            return indented_labels(t.left, d - 1) + \
              indented_labels(t.right, d - 1)

        for d in range(1, self.depth() + 1):
            cur_indent = 0
            for il in indented_labels(self, d):
                (indent, label) = il
                ls = str(label)
                spaces = indent - cur_indent
                assert spaces >= 0
                print(" " * spaces, end="")
                print(ls, end="")
                cur_indent += spaces + len(ls)
            print()


demo_tree = Tree(1, Tree(2, Tree(4, None, Tree(5))), Tree(3))

if __name__ == "__main__":
    print("testing demo tree")
    assert demo_tree.depth() ==  4
    assert demo_tree.nodes() == 5
    assert demo_tree.frontier() == [5, 3]
    assert demo_tree.widths() == [1, 2, 1, 1]
    assert demo_tree.sum() == 15
    demo_tree.print(end="")
    print()
    demo_tree.pretty_print()
