#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import re
import pandas as pd

os.listdir()


def mapper(review):
    review = review.strip()
    review = review.lower()
    review = re.findall("[a-z]+",review)
    return review
    
def reduce(review):
    word_count = {}
    for word in review:
        word_count[word]= review.count(word)
    return word_count




def map_reduce(file_name):
    with open (file_name,"r") as file:
        review = file.read()
        
    mapped = mapper(review)
    reducer = reduce(mapped)
    
    x1,x2 = [],[]
    for word,count in reducer.items():
        x1.append(word)
        x2.append(count)
    return x1, x2



y1, y2 = map_reduce("sample.txt")


dict1 = {"count":y2}
pd.DataFrame(dict1,index=y1)


# ## 📝 Word Count Using MapReduce Simulation in Python
# 
# This Python program simulates a basic **MapReduce job** for **counting word frequencies** in a text file (`sample.txt`), inspired by Hadoop’s MapReduce model.
# 
# ---
# 
# ### 🔧 Functions Explained
# 
# #### 🔹 `mapper(review)`
# - **Purpose**: Prepares and cleans the text.
# - **Operations**:
#   - Converts the entire text to lowercase.
#   - Uses regular expressions to extract only alphabetic words (removes punctuation/numbers).
# - **Returns**: A list of words.
# - ✅ *Example*:  
#   Input: `"Python is Fun!"`  
#   Output: `['python', 'is', 'fun']`
# 
# ---
# 
# #### 🔹 `reduce(review)`
# - **Purpose**: Aggregates the number of times each word appears.
# - **Operations**:
#   - Iterates over the list of words.
#   - Uses `.count()` to calculate frequency of each word.
# - **Returns**: A dictionary with word counts.
# - ✅ *Example*:  
#   Input: `['python', 'is', 'python']`  
#   Output: `{'python': 2, 'is': 1}`
# 
# ---
# 
# #### 🔹 `map_reduce(file_name)`
# - **Purpose**: Reads the file and runs the Map and Reduce phases.
# - **Operations**:
#   - Opens and reads the input text file.
#   - Passes text through `mapper()` and `reduce()`.
#   - Extracts words and their counts into two separate lists: `x1` (words) and `x2` (counts).
# - **Returns**: The two lists to be used for visualization or further processing.
# 
# ---
# 
# #### 🔹 `pandas.DataFrame`
# - **Purpose**: Converts the word count data into a clean, tabular format.
# - **Operations**:
#   - Creates a DataFrame with words as index and their frequencies as values.
# 
# ---
# 
# ### 📊 Sample Output
# 
# If `sample.txt` contains:
# 
# 
# Then the DataFrame will look like:
# count
#        
# python 2
# is 2
# fun 1
# powerful 1
# 
# 
# 
# ---
# 
# ### 🔗 Relation to Hadoop MapReduce
# 
# > In Hadoop MapReduce, the **mapper** emits key-value pairs like `('word', 1)`, and the **reducer** aggregates these values to compute totals.  
# > This program simulates that logic in Python:
# > - `mapper()` acts like the map phase (data preparation).
# > - `reduce()` aggregates word counts like the reduce phase.
# > Although it runs locally, it mimics the core concept of distributed processing used in Hadoop.
# 
# ---
# 
# 
# 

# In[ ]:




