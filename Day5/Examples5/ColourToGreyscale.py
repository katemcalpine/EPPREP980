#--------------------------------------------------------------------
# Title: ColourToGreyscale.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 5th December, 2023
# Found in: Day 5 Lecture Slides
#--------------------------------------------------------------------

import matplotlib.image as img
import matplotlib.pyplot as plt

a = img.imread('ColourImage.png')

plt.imshow(a)
plt.show()

r = a[:,:,0]
g = a[:,:,1]
b = a[:,:,2]

new = (r*0.3)+(g*0.59)+(b*0.11)

plt.imshow(new, cmap = 'gray')
plt.show()

#plt.imshow(new)
#plt.show()