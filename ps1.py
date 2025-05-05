#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from xmlrpc.server import SimpleXMLRPCServer

def compute_factorial(number):
    
    result = 1

    if number > 1:
        for i in range(1,number+1):
            result *= i
        return result
    
    return result

server = SimpleXMLRPCServer(("localhost",8000))

print("Server listening on port 8000")

server.register_function(compute_factorial, 'compute_factorial')
server.serve_forever()





import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")

number = int(input("Enter an integer to compute factorial for: "))

result = server.compute_factorial(number)

print(f"The factorial of {number} is {result}")


# . RPC (Remote Procedure Call) is a way for programs on different computers to talk to each 
# other over a network. It works like a regular function call but it happens between processes 
# running on different machines. It helps distributed systems communicate by allowing one 
# program to call a function on another program running on a different machine. 
# 
# 2. In an RPC system, there are typically two main components: the client and the server. The 
# client sends a request to the server, which executes the requested procedure and sends back 
# the result to the client. 
# 
# 3. Client-server interaction involves the client sending a request to the server, which then 
# processes the request and sends a response back to the client. This interaction follows a 
# specific protocol, such as HTTP or TCP/IP, to ensure communication between the client and 
# server. 
# 
# 4. Scalability and load balancing in distributed applications involve distributing incoming 
# requests evenly across multiple servers to prevent any single server from becoming overloaded. 
# Techniques like load balancers and clustering help manage increased traffic and maintain 
# system performance. 
# 
# 5. RPC offers simplicity and ease of use, but it may suffer from performance issues and tight 
# coupling between client and server. Other protocols like REST or messaging systems offer more 
# flexibility but might require more effort to set up and maintain. 
# 
# 
# 
# 
# - RPC (Remote Procedure Call) and RMI (Remote Method Invocation) are both mechanisms for invoking code on remote systems, but they differ mainly in their approach and language support.
# 
# RPC is language-independent and procedure-based—it allows a program to call a function on another system as if it were local, usually using simple data types.
# 
# - RMI, on the other hand, is Java-specific and object-oriented. It allows a Java program to call methods on a remote Java object and even pass objects as parameters using serialization.
# 
# In short:
# 
# RPC works with functions and primitive data types across different languages.
# 
# RMI works with Java objects and methods, and requires both client and server to be in Java.

# In[ ]:




