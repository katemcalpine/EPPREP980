#--------------------------------------------------------------------
# Title: 3DWhileLoop.py
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

plane = 0
while (plane < 3):
    row = 0
    while (row < 2):
        column = 0
        while (column < 11):
            b[plane, row, column] = a[plane, row, column] + 2
            column = column + 1
        row = row + 1
    plane = plane + 1
print(b)