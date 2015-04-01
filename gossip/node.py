class Node(object):
  def __init__(self, vector,my_id, last_matched_id):
      self.vector = vector
      self.my_id = my_id
      self.last_matched_id = last_matched_id
  
  def get_info(self):
      return self.my_id, self.last_matched_id, self.vector

  def __repr__(self):
        return "<my id %s target id:%s>" % (self.my_id, self.last_matched_id)
