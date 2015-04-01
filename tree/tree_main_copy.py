import random
import simpy
import matplotlib.pyplot as plt
import numpy
from link import *
from tree_node import *

lambd = 1

def get_pareto_delay():
   s = numpy.random.pareto(5, 1)
   return s[0]  

def get_exponential_delay():
  return random.expovariate(lambd)

def construct_link(env, event, node, outgoing_node):
   delay = get_pareto_delay()
   link = Link(env, delay, event, node, outgoing_node)
   return link

def construct_graph(num_nodes):
 graph = dict()
 for i in range(num_nodes,1,-1): 
    graph[i] = [i/2]
 graph[1] = []
 return graph

def construct_dicts(env, graph):
  inc_dict_a = dict()
  inc_dict_b = dict()
  out_dict_a = dict()
  out_dict_b = dict()
  for node,outgoing_nodes in graph.iteritems():
      outgoing_links_a = []
      incoming_events_b = []
      for outgoing_node in outgoing_nodes:
          delay = get_pareto_delay()
	  event_a = env.event()
	  event_b = env.event()
	  link_a = Link(env, delay,event_a, node, outgoing_node)
	  link_b = Link(env, delay,event_b, outgoing_node, node)
	  outgoing_links_a.append(link_a)
	  incoming_events_b.append(event_b)
	  inc_events_a = inc_dict_a.get(outgoing_node,[])
	  inc_events_a.append(event_a)
	  inc_dict_a[outgoing_node] = inc_events_a
          outer_events_b = out_dict_b.get(outgoing_node,[])
	  outer_events_b.append(link_b)
	  out_dict_b[outgoing_node] = outer_events_b
      out_dict_a[node] = outgoing_links_a
      inc_dict_b[node] = incoming_events_b
  return inc_dict_a,inc_dict_b, out_dict_a, out_dict_b
	    
def construct_tree_nodes(env, inc_dict_a,inc_dict_b, out_dict_a, out_dict_b):    
    for node in out_dict_a:
	incoming_events_a = inc_dict_a.get(node, [])
	outgoing_links_a =  out_dict_a.get(node,[])
        incoming_events_b = inc_dict_b.get(node, [])
	outgoing_links_b =  out_dict_b.get(node,[])
	tree = Tree(env, incoming_events_a,incoming_events_b, outgoing_links_a,outgoing_links_b, node)	

def run_test(num_nodes):
   graph = construct_graph(num_nodes)
   env = simpy.Environment()
   inc_dict_a,inc_dict_b,  out_dict_a, out_dict_b = construct_dicts(env, graph)
   construct_tree_nodes(env, inc_dict_a,inc_dict_b, out_dict_a, out_dict_b)
   env.run()
   return env.now

def run_multiple_tests(num_nodes):
    average_time = 0.0
    num_samples = 100
    for i in range(num_samples):
       time = run_test(num_nodes)
       average_time = (average_time * i + time)/(i+1)
    return average_time

def run():
   num_nodes_list = [3, 7, 15, 31, 63,127,255,511,1023,2047,4095,8191]
   times_list = []
   for num_nodes in num_nodes_list:
      average_time = run_multiple_tests(num_nodes) 
      print average_time
      times_list.append(average_time) 
   print times_list
   plt.plot(num_nodes_list, times_list, 'ro')
   plt.ylabel('time')
   plt.xlabel('num nodes')
   plt.show()
run()
