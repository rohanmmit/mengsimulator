import simpy

class Link(object):
  def __init__(self, env, delay, event, sender, receiver):
        self.env = env
        self.delay = delay
	self.event = event
	self.sender = sender
	self.receiver = receiver

  def fire(self):
       self.env.timeout(self.delay)
       print "did the timeout", self.sender, self.receiver
       self.event.succeed()         
