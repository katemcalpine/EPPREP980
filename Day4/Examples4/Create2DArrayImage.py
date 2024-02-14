#--------------------------------------------------------------------
# Title: Create2DArrayImage.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 30th November, 2023
# Found in: Day 4 Lecture Slides
#--------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

a = np.ones((9,9))

a[1:8,1:8] = 0

print(a)
plt.imshow(a)
plt.show()

plt.imshow(a, cmap = 'Greys')
plt.show()

plt.imshow(a, cmap = 'gray')
plt.show()

plt.imsave('BWImage.jpg', a, cmap = 'gray')