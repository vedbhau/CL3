#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

num_cities = 10
num_iterations = 100
num_ants = 100
alpha = 1
beta = 2
evaporation_rate = 0.1


pheromone_matrix = np.ones((num_cities, num_cities))
distance_matrix = np.random.randint(1,100,(num_cities,num_cities))
np.fill_diagonal(distance_matrix,0)



for i in range(num_iterations):
    for ant in range(num_ants):
        tour = []
        visited = set()
        current_city = np.random.randint(0,num_cities)
        tour.append(current_city)
        visited.add(current_city)
        
        for _ in range(num_cities-1):
            next_city_probability = [(pheromone_matrix[current_city][city]**alpha)*                                    ((1/distance_matrix[current_city][city])**beta)                                    if city not in visited else 0 for city in range(num_cities)]
            next_city_probability /= np.sum(next_city_probability)
            next_city = np.random.choice(num_cities, p=next_city_probability)
            tour.append(next_city)
            visited.add(next_city)
            current_city = next_city
            
        tour_length = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        pheromone_matrix += (1/tour_length)
    
    pheromone_matrix*=(1-evaporation_rate)
    
    
best_tour_length = np.inf
for ant in range(num_ants):
    tour_length = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    if tour_length<best_tour_length:
        best_tour_length = tour_length
        
print(best_tour_length)


# In[ ]:




