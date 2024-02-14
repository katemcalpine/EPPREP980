#--------------------------------------------------------------------
# Title: 2DForLoop.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 30th November, 2023
# Found in: Day 4 Lecture Slides
#--------------------------------------------------------------------

import numpy as np

a = np.array([np.linspace(0, 1, 11), np.linspace(1, 2, 11)])
print(a)
b = np.zeros((2, 11))

row = 0
for r in range(0, 2, 1):
    column = 0
    for c in range(0, 11, 1):
        b[row, column] = a[row, column] + 2
        column = column + 1
    row = row + 1
print(b)