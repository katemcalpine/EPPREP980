#--------------------------------------------------------------------
# Title: D3Q2.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 14th February, 2024
# Found in: Day 3 Tutorial Slides
#--------------------------------------------------------------------

import numpy as np

x = np.array([0,1,0,0,0,0,0,0,0])

# Long way:
x[2] = x[0] + x[1]
x[3] = x[1] + x[2]
x[4] = x[2] + x[3]
x[5] = x[3] + x[4]
x[6] = x[4] + x[5]
x[7] = x[5] + x[6]
x[8] = x[6] + x[7]
print(x)

# Quicker way:
for index in range(2, len(x)):
        x[index] = x[index-1] + x[index-2]
print(x)
