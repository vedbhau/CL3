#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Importing Libraries and Initialize Servers

import random

# List of available servers
servers = ["Server1", "Server2", "Server3"]


     
## Defining Random and Round Robin Load Balancer

# Round Robin Load Balancer
class RoundRobinLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    def get_server(self):
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server

# Random Load Balancer
class RandomLoadBalancer:
    def __init__(self, servers):
        self.servers = servers

    def get_server(self):
        return random.choice(self.servers)


     
## Simulating Client Requests

def simulate_requests(load_balancer, num_requests):
    for i in range(1, num_requests + 1):
        server = load_balancer.get_server()
        print(f"Request {i} routed to {server}")


     
## Output

if __name__ == "__main__":
    print("Round Robin Load Balancing:")
    round_robin_lb = RoundRobinLoadBalancer(servers)
    simulate_requests(round_robin_lb, 10)

    print("\nRandom Load Balancing:")
    random_lb = RandomLoadBalancer(servers)
    simulate_requests(random_lb, 10)


# In[ ]:




