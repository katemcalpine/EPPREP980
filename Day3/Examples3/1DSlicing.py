#--------------------------------------------------------------------
# Title: 1DSlicing.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 20th November, 2023
# Found in: Day 2 Lecture Slides
#--------------------------------------------------------------------

import numpy as np

a = np.array([12, 37, 24, 12, 42])

print(a)

#Capture index 1, 2, 3, 4
print(a[1:5])
#Capture index 0, 1, 2
print(a[:3])
# Capture index 3, 4
print(a[3:])

b = a[1:3]
print(b)
