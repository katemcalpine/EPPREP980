#--------------------------------------------------------------------
# Title: D2Q4.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 14th February, 2024
# Found in: Day 2 Tutorial Slides
#--------------------------------------------------------------------

import numpy as np

v = 5
g = 9.81

t = np.linspace(0, 2, 1001)
y = v*t - 0.5*g*t**2

# Easy way:
print(y[100])

# Difficult way:
print(v*t[100] - 0.5*g*t[100]**2)