#--------------------------------------------------------------------
# Title: SizeLength.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 5th December, 2023
# Found in: Day 5 Lecture Slides
#--------------------------------------------------------------------

import numpy as np

a = np.array([[[12, 37, 24], [12, 42, 5], [36, 7, 13]],
              [[61, 8, 56], [4, 54, 76], [34, 9, 23]],
              [[47, 9, 93], [2, 23, 54], [63, 42, 32]]])
print(a)
# Return total number of values in matrix
print(np.size(a))
# Return dimensions of matrix in format (row, column)
print(np.shape(a))
# Return number of rows in matrix, or length in 1D Array
print(len(a))
# Return number of columns in matrix
print(len(a[0]))
# Return number of planes in matrix
print(len(a[0,0]))