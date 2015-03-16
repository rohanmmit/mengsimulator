class Node(object):
  def __init__(self, value,id, last_matched_id):
      self.value = value
      self.id = id
      self.last_matched_id = last_matched_id
  
  def get_id(self):
      return self.id

  def get_last_matched_id(self):
      return self.last_matched_id
