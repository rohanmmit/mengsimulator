import simpy

class EventWrapper(object):
   
   def __init__(self,event):
     print "enters into init"
     self.event = event
   
   def set_event(self, event):
      self.event = event
   
   def get(self):
      return self.event 
