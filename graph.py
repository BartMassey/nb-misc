# Copyright © 2014 Bart Massey
# Markable graph node class.

class Node(object):
    def __init__(self, label):
        self.label = label
        self.marked = False

    def clear_mark(self):
        self.marked = False

    def set_mark(self):
        self.marked = True

    def is_marked(self):
        return self.marked

class Graph(object):
    def __init__(self, nodes, edges, weights):
        self.nodes = nodes
        self.edges = edges
        self.weights = weights
    
