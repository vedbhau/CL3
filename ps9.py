#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Implementation of Clonal selection algorithm using Python.

# Importing Libraries

import numpy as np


     
# Step 1: Defining Objective function

# Example: minimize f(x) = x^2)
def objective_function(x):
    return x**2


     
#------------------------------------------------------------------------------------------------------------
# Step 2: Clonal Selection Algorithm

def clonal_selection_algorithm(population_size, num_clones, mutation_rate, num_generations, search_space):
    # Initialize population
    population = np.random.uniform(search_space[0], search_space[1], population_size)
    
    for generation in range(num_generations):
        # Evaluate fitness
        fitness = np.array([objective_function(x) for x in population])
        
        # Select best antibodies
        sorted_indices = np.argsort(fitness)
        selected_antibodies = population[sorted_indices[:num_clones]]
        
        # Clone and mutate
        clones = np.repeat(selected_antibodies, num_clones)
        mutations = np.random.normal(0, mutation_rate, clones.shape)
        clones = clones + mutations
        clones = np.clip(clones, search_space[0], search_space[1])  # Ensure clones stay within search space
        
        # Replace population
        population = np.concatenate((clones, np.random.uniform(search_space[0], search_space[1], population_size - num_clones)))
        
        # Track best solution
        best_fitness = np.min(fitness)
        best_solution = population[np.argmin(fitness)]
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}, Best Solution = {best_solution}")
    
    return best_solution, best_fitness


     
#------------------------------------------------------------------------------------------------------------
# Step 3: Setting Parameters

# Parameters
population_size = 20
num_clones = 5
mutation_rate = 0.1
num_generations = 50
search_space = (-10, 10)  # Define the search space for x


     
#------------------------------------------------------------------------------------------------------------
# Step 4: Extracting Best Solution

best_solution, best_fitness = clonal_selection_algorithm(population_size, num_clones, mutation_rate, num_generations, search_space)
print("\nFinal Result:")
print(f"Best Solution: {best_solution}")
print(f"Best Fitness: {best_fitness}")


# "In this program, I have implemented the Clonal Selection Algorithm (CSA) in Python **to solve an optimization problem** — specifically to minimize a given objective function, which is f(x) = x². The goal is to find the value of x that **gives the smallest output of this function."**
# 
# ✅ What is the Clonal Selection Algorithm (CSA)?
# "CSA is inspired by how the **immune system works**, especially how it **produces antibodies** to fight infections. In simple terms:
# 
# The algorithm mimics how the immune system **selects the best antibodies, clones them, mutates them slightly, and selects the best of the new ones.**
# 
# This helps in solving optimization problems by **continuously improving the candidate solutions over generations."**
# 
# ---------------------------------------------------------------------------------------------------------------
# 
# ✅ Step 1: Importing Libraries
# We import the numpy library, which is used for generating random numbers, creating arrays, and performing mathematical operations efficiently.
# 
# ✅ Step 2: Defining the Objective Function
# We define a simple function f(x) = x², which we want to minimize. The goal is to find the value of x where this function gives the smallest value, which is at x = 0.
# 
# ✅ Step 3: Clonal Selection Algorithm Function
# We create a function called clonal_selection_algorithm that simulates the process of natural immune selection.
# 
# 1. Initialize Population
# We start by generating a random population of numbers (solutions) within a defined range. These act like "antibodies" in the immune system.
# 
# 2. Evaluate Fitness
# We calculate the fitness of each solution using the objective function. Lower values of x² indicate better fitness.
# 
# 3. Select Best Antibodies
# We sort the population by fitness and select the top few best solutions. These are considered the best antibodies.
# 
# 4. Clone and Mutate
# We make multiple copies (clones) of the best solutions and slightly change them using random noise (mutation). This allows us to explore nearby possible solutions.
# 
# 5. Replace Population
# We create a new population by combining the mutated clones with some fresh random solutions. This keeps the search diverse and avoids getting stuck in local minima.
# 
# 6. Track Best Solution
# We keep track of the best solution in each generation and print it. Over multiple generations, the algorithm gradually improves.
# 
# ✅ Step 4: Set Parameters
# We define important parameters like:
# 
# Population size (number of solutions),
# 
# Number of clones to select,
# 
# Mutation rate (how much we change each clone),
# 
# Number of generations (iterations),
# 
# Search space (range of values for x).
# 
# ✅ Step 5: Run the Algorithm
# Finally, we call the function with the parameters and display the best solution and its fitness after all generations.
# 
# 

# In[ ]:




