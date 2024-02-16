#--------------------------------------------------------------------
# Title: Referencing3DArray.py
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

print(a[0,0,1])