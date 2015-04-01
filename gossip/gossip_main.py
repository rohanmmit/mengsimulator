import math
import random
import matplotlib.pyplot as plt
import numpy
from heapq import heappush, heappop
from node import *
from match import *
error_cutoff = 0.05
lambd = 1

def is_close(vector, mean_vector):
  mean_sum = numpy.linalg.norm(mean_vector, 2) 
  diff = numpy.linalg.norm(vector-mean_vector, 2)
  if diff < error_cutoff * mean_sum:
      return True
  return False

def get_pareto_delay():
   s = numpy.random.pareto(5, 2)
   return (s[0] + s[1]) 

def get_exponential_delay():
  return random.expovariate(lambd) * 2

def setup(num_nodes):
  available_nodes = []
  unfinished_nodes = dict()
  vector_size = 1000
  mean_vector = [0.0] * vector_size
  for i in range(num_nodes):
    node_vector = []
    unfinished_nodes[i] = 0
    for j in range(vector_size): 
      value = random.random()
      node_vector.append(value)
      mean_vector[j] = (mean_vector[j] * i + value)/(i + 1)
    np_array = numpy.array(node_vector)
    node = Node(np_array,i, None)
    available_nodes.append(node)
  wrapped_mean_vector = numpy.array(mean_vector)
  return available_nodes, unfinished_nodes, wrapped_mean_vector

def process_match(match, available_nodes, unfinished_nodes, mean_vector):
   node1, node2 = match.get_nodes()
   node1_id, _, node1_vector = node1.get_info()
   node2_id, _, node2_vector = node2.get_info()
   new_vector = (node1_vector + node2_vector) / 2
   node1 = Node(new_vector, node1_id, node2_id)
   node2 = Node(new_vector, node2_id, node1_id)
   if is_close(new_vector, mean_vector):
	unfinished_nodes.pop(node1_id, None)
	unfinished_nodes.pop(node2_id, None)
   else :
	unfinished_nodes[node1_id] = 0
	unfinished_nodes[node2_id] = 0
   available_nodes.append(node1)  
   available_nodes.append(node2)  

def match_nodes(available_nodes, event_processing, current_time, limit):
    if len(available_nodes) < limit:
       return
    i = 0
    while i < len(available_nodes) - 1:
       current_node = available_nodes[i]
       _,_, vector = current_node.get_info()
       max_index = i + 1
       max_difference = -1
       for j in range(i+1, len(available_nodes)):
          temp_node = available_nodes[j]
          _, _,temp_node_vector = temp_node.get_info()
	  diff = numpy.linalg.norm(vector-temp_node_vector, 2)
	  if diff > max_difference:
             max_difference = diff
	     max_index = j  
       temp_node = available_nodes.pop(max_index)
       available_nodes.pop(i)
       random_delay = get_exponential_delay() + current_time
       new_match = Match(current_node, temp_node)
       heappush(event_processing, (random_delay,new_match))        
def run_test(num_nodes):
    available_nodes, unfinished_nodes, mean = setup(num_nodes)
    current_time = 0.0
    event_processing = []
    limit = math.floor(num_nodes * 0.1)
    while len(unfinished_nodes) != 0:
       match_nodes(available_nodes, event_processing, current_time, limit)
       new_time, match = heappop(event_processing)     
       current_time = new_time
       process_match(match,  available_nodes, unfinished_nodes, mean)
    return current_time

def run_multiple_tests(num_nodes):
    average_time = 0.0
    num_samples = 100
    for i in range(num_samples):
       time = run_test(num_nodes)
       average_time = (average_time * i + time)/(i+1)
    print average_time
    return average_time

def run():
   
   num_nodes_list = [3, 7, 15, 31, 63,127,255,511,1023,2047,4095,8191]
   times_list = []
   for num_nodes in num_nodes_list:
      average_time = run_multiple_tests(num_nodes) 
      times_list.append(average_time) 
   print times_list
   plt.plot(num_nodes_list, times_list)
   plt.ylabel('time')
   plt.xlabel('num nodes')
   plt.show()
run()
