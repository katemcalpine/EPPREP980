#--------------------------------------------------------------------
# Title: SizeLength.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 30th November, 2023
# Found in: Day 4 Lecture Slides
#--------------------------------------------------------------------

import numpy as np

a = np.array([[12, 37, 24], [12, 42, 5]])

print(a)

# Return total number of values in matrix
print(np.size(a))
# Return size of matrix in format (row,column)
print(np.shape(a))
# Return number of rows in matrix, or length in 1D array
print(len(a))
# Return number of columns in matrix
print(len(a[0]))


