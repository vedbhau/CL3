#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random 
import warnings
from deap import algorithms, base, creator, tools
warnings.filterwarnings("ignore")


# In[4]:


def eval_func(individuals):
    return sum(x**2 for x in individuals),

creator.create("FitnessMin", base.Fitness, weights = (-1.0,))
creator.create("Individual", list, fitness = creator.FitnessMin)
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -5.0, 5.0)
toolbox.register("Individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
toolbox.register("population", tools.initRepeat, list, toolbox.Individual)
toolbox.register("mate", tools.cxBlend, alpha = 0.5)
toolbox.register("mutate", tools.mutGaussian, mu = 0, sigma = 1, indpb = 0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", eval_func)

population = toolbox.population(n=50)
algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.1, ngen=20)

best_ind = tools.selBest(population, k=1)[0]
best_fit = best_ind.fitness.values[0]

print("Best individual:", best_ind)
print("Best fitness:", best_fit)


# DEAP stands for Distributed Evolutionary Algorithms in Python. It is a Python library used for implementing evolutionary algorithms like genetic algorithms, genetic programming, and evolution strategies. DEAP makes it easy to define individuals, populations, and apply genetic operators like crossover, mutation, and selection to solve optimization problems.
# 
# ✅ Q: What have you done in this code?
# Answer:
# 
# In this code, I have implemented a Genetic Algorithm using the DEAP library to minimize a mathematical function — specifically, the sum of squares of a list of float values (genes in an individual).
# 
# -----------------------------------------------------------------------------------------------------------------
# 
# 
# Then break it down like this:
# 
# Defined an evaluation function:
# 
# I wrote a function eval_func that calculates the fitness of an individual by summing the square of its elements. The goal is to minimize this sum, so lower values are better.
# 
# Used DEAP’s creator module:
# 
# I created a FitnessMin class to represent minimization problems.
# 
# Then, I created an Individual class which is just a list of numbers with a fitness attached.
# 
# Configured the toolbox:
# 
# I registered how each gene in the individual should be created using random.uniform(-5, 5).
# 
# Then I defined how to generate an entire individual (with 3 genes), and how to make a population from many individuals.
# 
# I also registered genetic operators:
# 
# Crossover: using cxBlend.
# 
# Mutation: using Gaussian noise.
# 
# Selection: using tournament selection.
# 
# And finally, the evaluation function.
# 
# Ran the evolutionary algorithm:
# 
# I initialized a population of 50 individuals.
# 
# Then I used eaSimple, a built-in algorithm in DEAP, to evolve the population over 20 generations. During each generation, DEAP applies selection, crossover, and mutation to improve the fitness of the individuals.
# 
# Displayed results:
# 
# After evolution, I selected the best individual from the final population and printed it along with its fitness score

# In[ ]:




