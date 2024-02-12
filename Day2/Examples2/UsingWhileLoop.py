#--------------------------------------------------------------------
# Title: UsingWhileLoop.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 20th November, 2023
# Found in: Day 2 Lecture Slides
#--------------------------------------------------------------------

import numpy as np

a = np.linspace(0, 1, 11)
b = np.zeros(11)
counter = 0

while (counter < 11):
	b[counter] = a[counter] + 2
	counter = counter + 1

print(b)
