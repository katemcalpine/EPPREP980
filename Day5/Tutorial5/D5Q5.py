#--------------------------------------------------------------------
# Title: D5Q5.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 16th February, 2024
# Found in: Day 5 Lecture Slides
#--------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

a = plt.imread('SunflowerFilter.png')

plt.imshow(a)
plt.show()

r = a[:, :, 0]
g = a[:, :, 1]
b = a[:, :, 2]

r = r / 0.15
g = g / 0.55
b = b / 0.30

c = np.zeros((len(a), len(a[0]), 3), float)

c[:, :, 0] = r
c[:, :, 1] = g
c[:, :, 2] = b

plt.imshow(c)
plt.xticks([])
plt.yticks([])
plt.show()