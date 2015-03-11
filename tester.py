import simpy

class Runner(object):
    def __init__(self, env, event_list):
        self.env = env
        self.event_list = event_list
   	self.action = env.process(self.run()) 
    def run(self):
        while True:
            yield env.timeout(3)
	    self.event_list[0].succeed()
	    self.event_list[0] = env.event()

class Tree(object):
     def __init__(self, env, event_list,):
	self.env = env
	self.event_list = event_list
	self.action = env.process(self.run())
     def run(self):
        while True:
	   print "hey"
	   yield self.event_list[0]
	   print('Processingat %d' % self.env.now)	     


env = simpy.Environment()
event_list = []
event = env.event()
event_list.append(event)
tree = Tree(env,event_list)
runner = Runner(env,event_list)
env.run(until=15)
