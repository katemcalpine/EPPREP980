#--------------------------------------------------------------------
# Title: UsingLinspace3D.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 5th December, 2023
# Found in: Day 5 Lecture Slides
#--------------------------------------------------------------------

import numpy as np

# Normal spacing
a = np.array([[np.linspace(1, 2, 11), np.linspace(2, 3, 11)], [np.linspace(1, 2, 11), np.linspace(2, 3, 11)],
             [np.linspace(1, 2, 11), np.linspace(2, 3, 11)]])

print(a)

# Abnormal spacing
a = np.array([[np.linspace(1, 2, 10), np.linspace(2, 3, 10)], [np.linspace(1, 2, 10), np.linspace(2, 3, 10)],
             [np.linspace(1, 2, 10), np.linspace(2, 3, 10)]])

print(a)