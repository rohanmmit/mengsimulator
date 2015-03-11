import simpy

class Link(object):
  def __init__(self, env, delay, event):
        self.env = env
        self.delay = delay
	self.event = event

  def fire(self):
       self.env.timeout(delay)
       self.event.succeed()         
