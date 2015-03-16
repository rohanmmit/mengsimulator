import math
import random

from event_wrapper import *
from node import *

error_cutoff = 0.05

def is_close(value, mean):
  diff = math.abs(value - mean)
  if diff < error_cutoff * mean:
      return True
  return False

def create_vectors(num_vectors):
    for i in range(num_vectors): 

event_queue = Queue.Queue()
num_vectors = 100
vector_value = []
for i in range(num_vectors): 
   random.random 
        



