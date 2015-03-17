import math
import random
import matplotlib.pyplot as plt
from heapq import heappush, heappop
from node import *

error_cutoff = 0.05
lambd = 1

def is_close(value, mean):
  diff = math.abs(value - mean)
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
  return available_nodes,  

def run_test(num_nodes):
    return num_nodes

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
event_processing = []
heappush(event_processing, (5.2,"write code"))        
heappush(event_processing, (5.3,"fuck"))
result = heappop(event_processing)        
run()

