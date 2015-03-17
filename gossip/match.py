from node import *

class Match(object):
  def __init__(self, node1, node2):
      self.node1 = node1
      self.node2 = node2
  
  def get_nodes(self):
      return self.node1, self.node2

