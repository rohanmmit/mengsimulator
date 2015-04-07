import numpy
class Node(object):
  def __init__(self, vector,  my_id, last_matched_id, matrix):
      self.vector = vector
      temp = []
      chunk = 10
      length = len(vector) / chunk
      ##for i in range(length):
          ##result = numpy.mean(vector[i*chunk : (i + 1) * chunk])
          ##temp.append(result)
      self.compressed_vector = numpy.dot(vector, matrix)
      self.my_id = my_id
      self.last_matched_id = last_matched_id
      if my_id == last_matched_id:
	print "fuck fuck fuck", my_id
        
  def get_info(self):
      return self.my_id, self.last_matched_id, self.vector, self.compressed_vector

  def __repr__(self):
        return "<my id %s target id:%s>" % (self.my_id, self.last_matched_id)
