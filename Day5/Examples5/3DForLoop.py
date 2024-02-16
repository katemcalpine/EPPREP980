#--------------------------------------------------------------------
# Title: 3DForLoop.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 5th December, 2023
# Found in: Day 5 Lecture Slides
#--------------------------------------------------------------------

import numpy as np

a = np.array([[np.linspace(1, 2, 11), np.linspace(2, 3, 11)],
              [np.linspace(1, 2, 11), np.linspace(2, 3, 11)],
              [np.linspace(1, 2, 11), np.linspace(2, 3, 11)]])
b = np.zeros((3, 2, 11))

print(a)

plane = 0
for p in range(0, 3, 1):
    row = 0
    for r in range(0, 2, 1):
        column = 0
        for c in range(0, 11, 1):
            b[plane, row, column] = a[plane, row, column] + 2
            column = column + 1
        row = row + 1
    plane = plane + 1
print(b)