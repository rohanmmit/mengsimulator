class Node(object):
  def __init__(self, value,my_id, last_matched_id):
      self.value = value
      self.my_id = my_id
      self.last_matched_id = last_matched_id
  
  def get_id(self):
      return self.my_id

  def get_last_matched_id(self):
      return self.last_matched_id
