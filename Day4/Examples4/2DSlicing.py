#--------------------------------------------------------------------
# Title: 2DSlicing.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 30th November, 2023
# Found in: Day 4 Lecture Slides
#--------------------------------------------------------------------

import numpy as np

a = np.array([[12, 37, 24], [12, 42, 5], [36, 7, 13]])

print(a)

#Capture index (0,0),(0,1)
print(a[0,0:2])
#Capture index (1,0),(1,1)
print(a[1,:2])
# Capture index (2,0),(2,1)
print(a[2,1:])
# Capture index (1,1)
print(a[1:2, 1:2])
