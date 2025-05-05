#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import re

os.listdir()

def map_reduce(file_name):
    with open(file_name, "r") as file:
        review = file.read()
        
    #mapper
    mapped = re.split(r"[.,!]", review)
    mapped = {mapped[i].strip():i+1 for i in range(len(mapped))}
    for doc, doc_id in mapped.items():
        print(f"doc_ID[{doc_id}]: {doc}")
    
    #reducer
    total_sents = len(mapped)
    print(f"\ntotal number of sentences : {total_sents}")
    
    
map_reduce("sample.txt")


# In[ ]:





# In[ ]:




