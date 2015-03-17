import simpy

class Link(object):
  def __init__(self, env, delay, event, sender, receiver):
        self.env = env
        self.delay = delay
	self.event = event
	self.sender = sender
	self.receiver = receiver

  def fire(self):
       yield self.env.timeout(self.delay)
       self.event.succeed()         
