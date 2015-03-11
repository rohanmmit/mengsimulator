import link
import random
import simpy

VECTOR_SIZE = 100 ## number of elements in vector
VALUE_RANGE = 100.0 ## highest value range for element in vector
LATENCY_RANGE = 100.0 ## range from zero for bottleneck link
PROCESS_RANGE = 1.0 ## the process range

class Tree(object):
     def __init__(self, env, incoming_events, outgoing_links):
         self.env = env
	 self.vector = []
	 for i in range(VECTOR_SIZE):
	     random_value = random.random() * VALUE_RANGE
	     self.vector.append(random_value)
         # Start the run process everytime an instance is created.
         self.action = env.process(self.run())
	 self.incoming_events = incoming_events    	 
	 self.outgoing_links = outgoing_links 
 
     def process_data(self):
	 process_time = random.random() * PROCESS_RANGE
	 yield self.env.timeout(process_time)	 
     
     def send_outgoing_links():
	for link in self.links:
	   link.fire()    	     
          
 
     def run(self):
         while True:
	     yield AllOf(env, self.incoming_events)
	     yield self.env.process(self.process_data())
             print('Processingat %d' % self.env.now)
