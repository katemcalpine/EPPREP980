#--------------------------------------------------------------------
# Title: ColourMappingRGB.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 5th December, 2023
# Found in: Day 5 Lecture Slides
#--------------------------------------------------------------------

import matplotlib.image as img
import matplotlib.pyplot as plt

a = img.imread('ColourImage.jpg')

plt.imshow(a)
plt.show()

r = a[:,:,0]
g = a[:,:,1]
b = a[:,:,2]

plt.imshow(r, cmap = 'Reds')
plt.show()
plt.imshow(g, cmap = 'Greens')
plt.show()
plt.imshow(b, cmap = 'Blues')
plt.show()