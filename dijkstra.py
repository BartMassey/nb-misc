# Copyright © 2014 Bart Massey
# Dijkstra's Algorithm

from debug import *
import heap
from graph import *

# dijkstra(source, graph):
#    source.distance <- 0
#    source.back <- None
#    insert source into frontier
#    while frontier is not empty
#      target <- extract min from frontier
#      if target is already marked as visited
#        continue
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

    def comparator(v):
        return v.distance
    
    def maybe_label(v):
        if not v:
            return v
        return v.label

    frontier = heap.Heap(heap.minheap, len(graph.edges), compare=comparator)
    frontier.insert(V(source, 0, None))
    while not frontier.is_empty():
        target_v = frontier.extract()
        target = target_v.vertex
        if target.is_marked():
            assert target.distance <= target_v.distance
            continue
        target.distance = target_v.distance
        target.back = target_v.back
        target.set_mark()
        debug("dequeue", target.label, target.distance, \
              maybe_label(target.back))
        if target.label == dest:
            return
        for edge in graph.edges:
            if target not in edge:
                continue
            (v, v2) = edge
            if v == target:
                v = v2
            implied_distance = target.distance + graph.weights[edge]
            if v.is_marked():
                assert v.distance <= implied_distance
                continue
            debug("enqueue", v.label, implied_distance, target.label)
            frontier.insert(V(v, implied_distance, target))

if __name__ == "__main__":
    from sys import argv

    es = {}
    vs = set()
    for line in open("oregon-mileage-map.txt", "r"):
        (v1, v2, w) = line.split()
        vs |= {v1}
        vs |= {v2}
        es[tuple({v1, v2})] = int(w)
    vd = {v : Node(v) for v in vs}
    gns = set(vd.values())
    ges = set()
    gws = {}
    for e in es:
        (v1, v2) = e
        xe = tuple({vd[v1], vd[v2]})
        ges |= {xe}
        gws[xe] = es[e]
    g = Graph(gns, ges, gws)
    dest = None
    if len(argv) > 2:
        dest = argv[2]
    dijkstra(vd[argv[1]], g, dest)
    for v in vs:
        if v == argv[1]:
            continue
        vv = vd[v]
        if not vv.is_marked():
            print("unvisited", v)
            continue
        print("%s: next=%s  dist=%s" % (v, vv.back.label, vv.distance))
