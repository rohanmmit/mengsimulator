class EventObject(object):
  def __init__(self, vertex1, vertex2):
      self.vertex1 = vertex1
      self.vertex2 = vertex2
  
  def get_vertex_one(self):
      return self.vertex1

  def get_vertex_two(self):
      return self.vertex2
