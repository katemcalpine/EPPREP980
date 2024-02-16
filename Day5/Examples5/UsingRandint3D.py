#--------------------------------------------------------------------
# Title: UsingRandint3D.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 5th December, 2023
# Found in: Day 5 Lecture Slides
#--------------------------------------------------------------------

import numpy as np

np.random.seed(1)
a = np.array([[np.random.randint(1, 2, 10),
         np.random.randint(2, 3, 10)], [np.random.randint(2, 4, 10),
         np.random.randint(4, 6, 10)],
             [np.random.randint(2, 4, 10),
         np.random.randint(4, 6, 10)]])

print(a)