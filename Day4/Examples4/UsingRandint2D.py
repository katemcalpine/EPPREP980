#--------------------------------------------------------------------
# Title: UsingRandint2D.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 30th November, 2023
# Found in: Day 4 Lecture Slides
#--------------------------------------------------------------------

import numpy as np

np.random.seed(1)
a = np.array([np.random.randint(2, 4, 10), np.random.randint(4, 6, 10)])

print(a)