import simpy

class Link(object):
  def __init__(self, env, delay, event_wrapper, sender, receiver):
        self.env = env
        self.delay = delay
	self.event_wrapper = event_wrapper
	self.sender = sender
	self.receiver = receiver

  def fire(self):
       self.env.timeout(self.delay)
       self.event_wrapper.get().succeed()         
       event = self.env.event()
       self.event_wrapper.set_event(event)       
