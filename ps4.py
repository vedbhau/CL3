#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Pyro4
@Pyro4.expose

class PalindromeChecker():
    def is_palindrome(self, string):
        string = string.lower()
        return string==string[::-1]
    
daemon = Pyro4.Daemon()
uri = daemon.register(PalindromeChecker)
print(uri)
daemon.requestLoop()


# In[ ]:


import Pyro4

uri = input("enter uri of server")
is_palindrome_checker = Pyro4.Proxy(uri)

string_input = input("Enter string : ")
flag = is_palindrome_checker.is_palindrome(string_input)

if flag:
    print("Is a palindrome")
else:
    print("Not a palindrome")


# 🗣️ Q: What have you done in this program?
# Answer:
# 
# I have implemented a distributed application using Remote Method Invocation (RMI) concept in Python using the Pyro4 library. In this application, the client sends two strings to the server, and the server returns their concatenation.
# 
# 
# 
# 🗣️ Q: How does your program work?
# Answer:
# 
# The server hosts a class called StringConcatenator with a method concatenate(str1, str2) that joins the two strings and returns the result. This method is exposed for remote access using @Pyro4.expose.
# 
# The server runs a Pyro daemon which listens for remote calls. Once the object is registered, it prints a unique Pyro URL.
# 
# On the client side, I input the server's URL and use Pyro4.Proxy to create a proxy object. Then, I collect two strings from the user and call the remote concatenate() method. The result is returned by the server and displayed on the client side.
# 
# 
# 
# 🗣️ Q: What is RMI and how is it used here?
# Answer:
# 
# RMI, or Remote Method Invocation, is a way to invoke methods on an object that exists on a different machine or process, as if it were local. It is commonly used in distributed systems.
# 
# In this project:
# 
# - The server hosts the actual object and method.
# 
# - The client uses a proxy (like a stub) to call that method remotely.
# 
# - Pyro4 handles the communication between client and server over the network using a Pyro URL.
# 
# So, my program simulates RMI using Pyro4 in Python, where a method on a remote server is called from a local client.
# 
# 
# 
# 
# 
# Optional Points to Add (if asked for more):
# 
# This application shows how distributed systems can be used to offload computation.
# 
# The method call is seamless for the user — just like calling a local method.
# 
# Pyro4 abstracts the socket programming and networking complexity, making RMI-style development easier.

# In[ ]:




