import math
import random
import matplotlib.pyplot as plt
from heapq import heappush, heappop
from node import *
from match import *
error_cutoff = 0.05
lambd = 1

def is_close(value, mean):
  diff = abs(value - mean)
  if diff < error_cutoff * mean:
      return True
  return False

def isFinished(dic, mean):
  for _, value in dic.iteritems():
     if not is_close(value, mean): 
       return False
  return True

def get_delay():
  return 2 * random.expovariate(lambd)

def setup(num_nodes):
  available_nodes = []
  node_dict = dict()
  mean = 0.0
  for i in range(num_nodes): 
    value = random.random()
    node_dict[i] = value
    node = Node(value,i, None)
    available_nodes.append(node)
    mean = (mean * i + value)/(i + 1)
  return available_nodes, node_dict, mean 

def process_match(match, node_dict, available_nodes):
   node1, node2 = match.get_nodes()
   node1_id, _, node1_value = node1.get_info()
   node2_id, _, node2_value = node2.get_info()
   average = (node1_value + node2_value) / 2
   node_dict[node1_id] = average
   node_dict[node2_id] = average
   node1 = Node(average, node1_id, node2_id)
   node2 = Node(average, node2_id, node1_id)
   available_nodes.append(node1)  
   available_nodes.append(node2)  

def match_nodes(available_nodes, event_processing, current_time):
    i = 0
    while i < len(available_nodes):
       current_node = available_nodes[i]
       _,past_id, _ = current_node.get_info()
       for j in range(i+1, len(available_nodes)):
          temp_node = available_nodes[j]
          temp_node_id, _,_ = temp_node.get_info()
          if temp_node_id != past_id:
             available_nodes.pop(j)
             available_nodes.pop(i)
             random_delay = get_delay() + current_time
             new_match = Match(current_node, temp_node)
	     heappush(event_processing, (random_delay,new_match))        
             i = i -1
             break 
       i = i + 1     
def run_test(num_nodes):
    available_nodes, node_dict, mean = setup(num_nodes)
    current_time = 0.0
    event_processing = []
    while not isFinished(node_dict, mean):
       print node_dict 
       match_nodes(available_nodes, event_processing, current_time)
       new_time, match = heappop(event_processing)     
       current_time = new_time
       process_match(match, node_dict, available_nodes)
    print current_time
    return current_time

def run_multiple_tests(num_nodes):
    average_time = 0.0
    for i in range(num_nodes):
       time = run_test(num_nodes)
       average_time = (average_time * i + time)/(i+1)
    return average_time

def run():
   num_nodes_list = [10, 100, 1000, 10000]
   times_list = []
   for num_nodes in num_nodes_list:
      average_time = run_multiple_tests(num_nodes) 
      times_list.append(average_time) 
   plt.plot(num_nodes_list, times_list)
result = run_test(10)

