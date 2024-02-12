#--------------------------------------------------------------------
# Title: HistogramPlot2.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 25th November, 2023
# Found in: Day 3 Lecture Slides
#--------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

x = np.random.randint(0,11,100)

plt.hist(x, bins=5, color = ‘green’)
plt.title(‘Histogram’)
plt.ylabel(‘Frequency’)
plt.xlabel(‘Number in Array’)
plt.legend([‘Frequency’])
plt.grid(False)
plt.show()
