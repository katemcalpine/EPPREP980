#--------------------------------------------------------------------
# Title: HistogramPlot.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 25th November, 2023
# Found in: Day 3 Lecture Slides
#--------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

x = np.random.randint(0,11,100)

plt.hist(x)
plt.show()
