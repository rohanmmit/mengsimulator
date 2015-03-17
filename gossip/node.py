class Node(object):
  def __init__(self, value,my_id, last_matched_id):
      self.value = value
      self.my_id = my_id
      self.last_matched_id = last_matched_id
  
  def get_info(self):
      return self.my_id, self.last_matched_id, self.value

  def __repr__(self):
        return "<my id %s target id:%s>" % (self.my_id, self.last_matched_id)