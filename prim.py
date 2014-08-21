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
            return self.weights[edge]

        tree = set()
        target = self.nodes[0]
        frontier = heap.Heap(heap.minheap, len(self.edges), \
                             compare=edge_weight)

        def opposite_node(target, e):
            (v1, v2) = e
            if (v1 == target):
                return v2
            assert v2 == target
            return v1

        def add_frontier(target):
            for e in self.edges:
                if target not in e:
                    continue
                nt = opposite_node(target, e)
                if nt.is_marked():
                    continue
                frontier.insert(e)

        while True:
            target.set_mark()
            add_frontier(target)
            if frontier.is_empty():
                return tree
            next_edge = frontier.extract()
            (n1, n2) = next_edge
            if n1.is_marked() and n2.is_marked():
                continue
            tree |= {next_edge}
            target = n1
            if n1.is_marked():
                assert not n2.is_marked()
                target = n2

if __name__ == "__main__":
    test_nodes = [Node(i) for i in range(5)]
    ws = {(0, 2) : 7, (0, 3) : 11, (1, 2) : 1, \
          (1, 3) : 25, (1, 4) : 18, (2, 3) : 18, (2, 4) : 12}
    test_edges = set()
    test_weights = {}
    for (i, j) in ws:
        e = tuple({test_nodes[i], test_nodes[j]})
        test_edges |= {e}
        test_weights[e] = ws[(i, j)]
    g = MWSTGraph(test_nodes, test_edges, test_weights)
    mwst = g.mwst()
    print([(e[0].label, e[1].label) for e in mwst])
