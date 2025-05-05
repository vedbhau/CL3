#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

os.listdir()

def mapper(review):
    review = review.lower()
    review = review.split()
    review = "".join(review)
    return review

def reduce(review):
    char_count = {}
    for char in review:
        char_count[char] = review.count(char)
    return char_count


def map_reduce(file_name):
    with open(file_name, "r") as file:
        review = file.read()
    mapped = mapper(review)
    reduced = reduce(mapped)
    
    for char, count in reduced.items():
        print(f"char:{char} -> count:{count}")
        
map_reduce("ssd.txt")


# In[4]:


import os
import re

os.listdir()

def mapper(review):
    review = review.strip()
    review = review.lower()
    review = re.findall("[a-z]+", review)
    return review

def reduce(review):
    word_count = {}
    for word in review:
        word_count[word] = review.count(word)
    return word_count


def map_reduce(file_name):
    with open(file_name, "r") as file:
        review = file.read()
        
    mapped = mapper(review)
    reduced = reduce(mapped)
    
    for word, count in reduced.items():
        print(f"word:{word} -> count:{count}")
        
map_reduce("ssd.txt")


# 🔹What is Hadoop and MapReduce?
# 
# - 🟢 Hadoop System:
# Apache Hadoop is an open-source distributed computing framework.
# 
# It allows you to store and process large datasets across clusters of computers using simple programming models.
# 
# It has two main components:
# 
# HDFS (Hadoop Distributed File System): Stores large files across multiple nodes.
# 
# MapReduce: A programming model used to process data in parallel across many nodes.
# 
# ------------------------------------------------------------------------------------------------------------------
# 
# - 🟢 MapReduce Concept:
# MapReduce works in two phases:
# 
# Map Phase – Takes input data and converts it into key-value pairs.
# 
# Reduce Phase – Takes those key-value pairs and aggregates or processes them (e.g., sum counts).
# 
# It’s great for counting problems, like character count or word count.
# 
# 🔸How You Simulated MapReduce in Python:
# Note: You're not using actual Hadoop, but you have simulated the MapReduce logic locally using Python for:
# 
# - Character Count
# - Word Count
# 
# 

#  I’ve simulated a basic MapReduce job in Python, which mimics Hadoop’s MapReduce model. In Hadoop, the mapper transforms input into key-value pairs — for example, ('a', 1) or ('word', 1) — and the reducer then aggregates these pairs to count total occurrences.
# 
# In my code:
# 
# - The mapper() function prepares the data (either characters or words).
# 
# - The reduce() function simulates the reduce phase by aggregating the counts.
# 
# While this runs locally on a single machine, in real Hadoop systems, this would run on a distributed cluster where different chunks of data are mapped and reduced in parallel."
# 
# 

# In[6]:


import os

os.listdir()

def mapper(review):
    review = review.lower()
    review = review.split()
    review = "".join(review)
    return review
    
def reducer(review):
    char_count = {}
    for char in review:
        char_count[char] = review.count(char)
        
    return char_count

def MapRedcuce(file_name):
    with open(file_name,"r") as file:
        review = file.read()
        
    mapped = mapper(review)
    reduced = reducer(mapped)
    
    for char , count in reduced.items():
        print("character:",char," --> count is :",count)
        
MapRedcuce("ssd.txt")


# In[ ]:





# In[ ]:




