import link
import random
import simpy

VECTOR_SIZE = 100 ## number of elements in vector
VALUE_RANGE = 100.0 ## highest value range for element in vector
LATENCY_RANGE = 100.0 ## range from zero for bottleneck link
PROCESS_RANGE = 1.0 ## the process range

class Tree(object):
     def __init__(self, env, incoming_events_a, outgoing_links_a,incoming_events_b, outgoing_links_b, my_id):
         self.env = env
	 self.my_id = my_id
	 self.incoming_events_a = incoming_events_a 
	 self.incoming_events_b = incoming_events_b 
	 self.outgoing_links_a = outgoing_links_a
	 self.outgoing_links_b = outgoing_links_b
         self.action = env.process(self.run())
    
     def send_outgoing_links_a(self):
	for link in self.outgoing_links_a:
	   link.fire()   

     def send_outgoing_links_b(self):
	for link in self.outgoing_links_b:
	   link.fire()    	     
     
     def run(self):
        yield env.all_of(self.incoming_events_a)
	self.send_outgoing_links_a()
	yield env.all_of(self.incoming_events_b)
	self.send_outgoing_links_b()
        print(self.id,' Processingat %d' % self.env.now)
