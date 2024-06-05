#--------------------------------------------------------------------
# Title: UsingLinspace.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 20th November, 2023
# Found in: Day 2 Lecture Slides
#--------------------------------------------------------------------

import numpy as np

# Includes 1
a = np.linspace(0, 1, 11)

print(a)

# Does not include 1
a = np.linspace(0, 1, 10)

print('{:.3}'.format(a[len(a)-1]))
