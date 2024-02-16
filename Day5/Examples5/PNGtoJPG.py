#--------------------------------------------------------------------
# Title: PNGtoJPG.py
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

plt.imsave('ColourImage.jpg', a)

b = img.imread('ColourImage.jpg')

plt.imshow(b)
plt.show()