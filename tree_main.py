import simpy
import link
import tree_node


def construct_graph(filename):
    f = open(filename,"r")
    graph = dict()
    for line in f:
        values = line.split()
        node, links = values[0], values[1:]
        graph[node] = links
    return graph 

graph = construct_graph("examples/tree1.txt")
outwark_links = dict()
incoming_events = dict()
for key,value in graph.iteritems():
    print "the key is", key
    print "the value is", value
