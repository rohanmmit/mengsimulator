import simpy

from link import *
from tree_node import *


def construct_graph(filename):
    f = open(filename,"r")
    graph = dict()
    for line in f:
        values = line.split()
        node, links = values[0], values[1:]
        graph[node] = links
    return graph 

def construct_link(env, event):
   delay = 20
   link = Link(env, delay, event)
   return link

def construct_dicts(env, graph):
  inc_dict = dict()
  out_dict = dict()
  for node,outgoing_nodes in graph.iteritems():
      outgoing_links = []
      for outgoing_node in outgoing_nodes:
	  event = env.event()
	  link = construct_link(env, event)
	  outgoing_links.append(link)
	  inner_events = inc_dict.get(outgoing_node,[])
	  inner_events.append(outgoing_node)
	  inc_dict[outgoing_node] = inner_events
      out_dict[node] = outgoing_links
  return inc_dict, out_dict
	    
def construct_tree_nodes(env, inc_dict, out_dict):    
    for node in out_dict:
	incoming_events = inc_dict.get(node, [])
	outgoing_links =  out_dict.get(node)
	print "env before", env
	tree = Tree(env, incoming_events, outgoing_links)	
	print "env after", env
    return
graph = construct_graph("examples/tree1.txt")
env = simpy.Environment()
inc_dict, out_dict = construct_dicts(env, graph)
construct_tree_nodes(env, inc_dict, out_dict)
env.run()
