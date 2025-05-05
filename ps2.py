#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from xmlrpc.server import SimpleXMLRPCServer

def add(x,y): return x+y
def subtract(x,y): return x-y
def multiply(x,y): return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        raise ZeroDivisionError("Can not be divided by 0")
        
with SimpleXMLRPCServer(("localhost", 8000)) as server:
    print("Server is active")
    
    for func in [add, subtract, multiply, divide]:
        server.register_function(func, func.__name__)
        
    server.serve_forever()


# In[ ]:


import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

while True:
    choice = input("""
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division
    5.Exit
    """)
    
    if choice==5:
        break
        
    if choice not in "1 2 3 4 5".split():
        print("Invalid choice")
        continue
        
    x = float(input("Enter first number : "))
    y = float(input("Enter second number : "))
        
    result = getattr(proxy, "1 2 3 4 5".split()[choice-1](x,y))
    print(result)


# In[ ]:


. RPC (Remote Procedure Call) is a way for programs on different computers to talk to each 
other over a network. It works like a regular function call but it happens between processes 
running on different machines. It helps distributed systems communicate by allowing one 
program to call a function on another program running on a different machine. 

2. In an RPC system, there are typically two main components: the client and the server. The 
client sends a request to the server, which executes the requested procedure and sends back 
the result to the client. 

3. Client-server interaction involves the client sending a request to the server, which then 
processes the request and sends a response back to the client. This interaction follows a 
specific protocol, such as HTTP or TCP/IP, to ensure communication between the client and 
server. 

4. Scalability and load balancing in distributed applications involve distributing incoming 
requests evenly across multiple servers to prevent any single server from becoming overloaded. 
Techniques like load balancers and clustering help manage increased traffic and maintain 
system performance. 

5. RPC offers simplicity and ease of use, but it may suffer from performance issues and tight 
coupling between client and server. Other protocols like REST or messaging systems offer more 
flexibility but might require more effort to set up and maintain. 


# In[ ]:




