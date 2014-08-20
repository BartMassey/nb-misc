# Copyright © 2014 Bart Massey
# Prim's Algorithm

from graph import *
import heap

class MWSTGraph(Graph):
    def __init__(self, *args):
        super().__init__(*args)

    # Minimum-Weight Spanning Tree via Prim's Algorithm.
    # Builds up the tree by greedily adding a shortest frontier node.
    def mwst(self):
        def edge_weight(edge):
            return self.weights[tuple(edge)]

        tree = set()
        target = self.nodes[0]
        frontier = heap.Heap(heap.minheap, len(self.edges), \
                             compare=edge_weight)

        def opposite_node(target, e):
            return e.difference({target}).pop()

        def add_frontier(target):
            for e in self.edges:
                if target not in e:
                    continue
                nt = opposite_node(target, e)
                if nt.is_marked():
                    continue
                frontier.insert(e)

        while True:
            frontier = add_frontier(target)
            target.set_mark()
            next_edge = None
            while not frontier.is_empty():
                next_edge = frontier.extract()
                e = next_edge.copy()
                n1 = e.pop()
                n2 = e.pop()
                if not n1.is_marked() or not n2.is_marked():
                    break
                next_edge = None
            if next_edge == None:
                return tree
            tree |= {next_edge}
            target = opposite_node(target, next_edge)

if __name__ == "__main__":
    test_weights = {(0, 2) : 7, (0, 3) : 11, (1, 2) : 1, \
                    (1, 3) : 25, (1, 4) : 18, (2, 3) : 18, (2, 4) : 12}
    test_nodes = [Node(i) for i in range(5)]
    test_edges = [{test_nodes[i], test_nodes[j]} for (i, j) in test_weights]
    
