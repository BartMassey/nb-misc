# Copyright © 2014 Bart Massey
# Dijkstra's Algorithm

import heap
from graph import *

# dijkstra(source, graph):
#    source.distance <- 0
#    source.back <- None
#    insert source into frontier
#    while frontier is not empty
#      target <- extract min from frontier
#      mark target as visited
#      for every vertex v connected in graph to the target
#        implied_distance <- target.distance + edge weight from target to v
#        if v is marked as visited
#          assert v.distance <= implied_distance
#          continue
#        v.distance <- implied_distance
#        v.back <- target
#        insert v into the frontier


def dijkstra(source, graph, dest=None):
    for v in graph.nodes:
        v.clear_mark()

    source.distance = 0
    source.back = None

    class V(object):
        def __init__(self, vertex, distance, back):
            self.vertex = vertex
            self.distance = distance
            self.back = back

    def ordered(v1, v2):
        return v1.distance <= v2.distance
    
    frontier = heap.Heap(heap.minheap, len(graph.edges), compare=ordered)
    frontier.insert(V(source, 0, None))
    while not frontier.is_empty():
        target_v = frontier.extract()
        target = target_v.vertex
        target.distance = target_v.distance
        target.back = target_v.back
        if target == dest:
            return
        target.set_mark()
        for e in graph.edges:
            if target not in e:
                continue
            e = next_edge.copy()
            v = e.pop()
            if v == target:
                v = e.pop()
            implied_distance = target.distance + \
              graph.weights[tuple({target, v})]
            if v.is_marked():
                assert v.distance <= implied_distance
                continue
            frontier.insert(V(v, implied_distance, target))
