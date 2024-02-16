#--------------------------------------------------------------------
# Title: JPGExperiment.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 5th December, 2023
# Found in: Day 5 Lecture Slides
#--------------------------------------------------------------------

import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

a = img.imread('ColourImage.png')

print(np.shape(a))

plt.imshow(a)
plt.show()

print(a[:,:,1])

plt.imshow(a[:,:,1])
plt.show()