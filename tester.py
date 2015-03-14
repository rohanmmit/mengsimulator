import simpy

from event_wrapper import *
class Runner(object):
    def __init__(self, env, event):
        self.env = env
        self.event = event
   	self.action = env.process(self.run()) 
    def run(self):
        for i in range(2):
	    env = self.env
            yield env.timeout(3)
	    self.event.get().succeed()
	    self.event.set_event(env.event())

class Tree(object):
     def __init__(self, env, event):
	self.env = env
	self.event = event
	self.action = env.process(self.run())
     def run(self):
        for i in range(2):
	   print "hey"
	   yield self.event.get()
	   print('Processingat %d' % self.env.now)	     


env = simpy.Environment()
event = env.event()
wrapper = EventWrapper(event)
tree = Tree(env,wrapper)
runner = Runner(env,wrapper)
env.run()
print env.now
