#--------------------------------------------------------------------
# Title: VectorisationScaling.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 5th December, 2023
# Found in: Day 5 Lecture Slides
#--------------------------------------------------------------------

import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

a = img.imread('ColourImage.jpg')

plt.imsave('JPGtoPNG.png', a)
a = img.imread('JPGtoPNG.png')

plt.imshow(a)
plt.show()

#plt.imshow(a*5)
#plt.show()

print(np.shape(a))

plt.imshow(a*0.5)
plt.show()