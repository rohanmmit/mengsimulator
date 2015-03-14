import link
import random
import simpy

VECTOR_SIZE = 100 ## number of elements in vector
VALUE_RANGE = 100.0 ## highest value range for element in vector
LATENCY_RANGE = 100.0 ## range from zero for bottleneck link
PROCESS_RANGE = 1.0 ## the process range

class Tree(object):
     def __init__(self, env, incoming_events, outgoing_links, id):
         self.env = env
	 self.vector = []
	 self.id = id
	 for i in range(VECTOR_SIZE):
	     random_value = random.random() * VALUE_RANGE
	     self.vector.append(random_value)
         # Start the run process everytime an instance is created.
         self.action = env.process(self.run())
	 self.incoming_events = incoming_events    	 
	 self.outgoing_links = outgoing_links 
 
     def process_data(self):
	 process_time = random.random() * PROCESS_RANGE
	 yield self.env.timeout(10)	 
     
     def send_outgoing_links(self):
	for link in self.outgoing_links:
	   link.fire()    	     
         
     def generate_events_list(self, event_wrapper_list):
	events = []
	for event_wrapper in self.incoming_events:	 
 	    events.append(event_wrapper.get())
	return events
     def run(self):
         while True:
	     env = self.env
	     event_list = self.generate_events_list(self.incoming_events)
	     yield env.all_of(event_list)
	     yield self.env.process(self.process_data())
	     self.send_outgoing_links()
	     print(self.id,' Processingat %d' % self.env.now)
