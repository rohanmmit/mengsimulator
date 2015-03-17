import random
import simpy

from link import *
from tree_node import *

def get_delay():
  return random.expovariate(lambd)


def construct_link(env, event, node, outgoing_node):
   delay = get_delay()
   link = Link(env, delay, event, node, outgoing_node)
   return link

def construct_dicts(env, graph):
  inc_dict = dict()
  out_dict = dict()
  for node,outgoing_nodes in graph.iteritems():
      outgoing_links = []
      for outgoing_node in outgoing_nodes:
	  event = env.event()
	  link = construct_link(env, event, node, outgoing_node)
	  outgoing_links.append(link)
	  inner_events = inc_dict.get(outgoing_node,[])
	  inner_events.append(event)
	  inc_dict[outgoing_node] = inner_events
      out_dict[node] = outgoing_links
  return inc_dict, out_dict
	    
def construct_tree_nodes(env, inc_dict, out_dict):    
    for node in out_dict:
	incoming_events = inc_dict.get(node, [])
	outgoing_links =  out_dict.get(node)
	tree = Tree(env, incoming_events, outgoing_links, node)	
    return

def run_test(num_nodes):
   graph = construct_graph("examples/tree1.txt")
   env = simpy.Environment()
   inc_dict, out_dict = construct_dicts(env, graph)
   construct_tree_nodes(env, inc_dict, out_dict)
   env.run()
   return env.now()

def run_multiple_tests(num_nodes):
    average_time = 0.0
    num_samples = 10
    for i in range(num_samples):
       time = run_test(num_nodes)
       average_time = (average_time * i + time)/(i+1)
    return average_time

def run():
   num_nodes_list = [10, 100, 1000, 10000, 100000,1000000 ]
   times_list = []
   for num_nodes in num_nodes_list:
      average_time = run_multiple_tests(num_nodes) 
      times_list.append(average_time) 
   print times_list
   plt.plot(num_nodes_list, times_list)
run()


