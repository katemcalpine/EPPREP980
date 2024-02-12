#--------------------------------------------------------------------
# Title: ScatterPlot.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 25th November, 2023
# Found in: Day 3 Lecture Slides
#--------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x = np.array([5, 7, 8, 3, 4, 7, 9, 10, 1, 2])
y = np.array([14, 15, 23, 4, 10, 18, 12, 12, 16, 5])

plt.scatter(x, y)
plt.title('Scatter Plot')
plt.ylabel('Y Coordinate')
plt.xlabel('X Coordinate')
plt.legend(['Location'])
plt.grid(False)
plt.show()
