#--------------------------------------------------------------------
# Title: D4Q5.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 14th February, 2024
# Found in: Day 4 Tutorial Slides
#--------------------------------------------------------------------

import numpy as np
import Greyscale as gs
import matplotlib.pyplot as plt

a = np.zeros((5,5))
a[:,0] = 1
a[:,2] = 1
a[:,4] = 1

print(a)

gs.grey1(a)
gs.grey2(a)

plt.imsave('grey1.jpg', a, cmap = 'Greys')
plt.imsave('grey2.jpg', a, cmap = 'gray')