####################################################################
#   Approximating Pi Using Monte Carlo and Geometry
####################################################################

import math
import numpy as np
import pandas as pd
from random import random
import matplotlib.pyplot as plt

# Initialize lists to hold the random coordinates
#
inside_x = []
outside_x = []

inside_y = []
outside_y = []

iterations = 1000000

# Creates a set amount of random x and y coordinates 
#                    and checks if its in the circle

for i in range(0, iterations):
    
    x = random() * 100
    y = random() * 100
    
    y_max = math.sqrt(2500 - ((x - 50)**2)) + 50
    y_min = 50 - math.sqrt(2500 - ((x - 50)**2))
    
    if(y <= y_max and y >= y_min):
        inside_x.append(x)
        inside_y.append(y)
    else:
        outside_x.append(x)
        outside_y.append(y)
        
# Approximates Pi using the area of the circle divided by the overall area of the square 
#                                         times four Ac/As = pi * r^2 / 4 * r^2 = pi / 4

pi_approx = len(inside_x) * 4 / (len(inside_x) + len(outside_x))
print(pi_approx)

# Plots the Resuting coordinate pairs
#    
plt.style.use('seaborn-ticks')    
plt.figure(figsize=(10,10))

axes = plt.axes()
axes.set_ylim(0, 100)
axes.set_xticks(np.arange(0, 101, 5))
axes.set_yticks(np.arange(0, 101, 5))
    
plt.title(('Pi Approximation with ' + str(iterations) + ' iterations: ' + str(pi_approx)))
plt.ylabel("Y Axes")
plt.xlabel("X Axes")
    
plt.scatter(inside_x, inside_y, s=0.5)
plt.scatter(outside_x, outside_y, s=0.5)
plt.show()

