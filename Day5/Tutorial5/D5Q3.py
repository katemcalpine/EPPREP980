#--------------------------------------------------------------------
# Title: D5Q3.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 16th February, 2024
# Found in: Day 5 Lecture Slides
#--------------------------------------------------------------------

import matplotlib.pyplot as plt

a = plt.imread('SunflowerFilter.png')

plt.imshow(a)
plt.show()

r = a[:, :, 0]
g = a[:, :, 1]
b = a[:, :, 2]