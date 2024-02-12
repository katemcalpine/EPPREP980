#--------------------------------------------------------------------
# Title: ScatterPlot3.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 25th November, 2023
# Found in: Day 3 Lecture Slides
#--------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

x1 = np.array([5, 7, 8, 3, 4, 7, 9, 10, 1, 2])
y1 = np.array([14, 15, 23, 4, 10, 18, 12, 12, 16, 5])
x2 = np.random.randint(0,11,10)
y2 = np.random.randint(10,21,10)

plt.scatter(x1, y1, color = ‘green’)
plt.scatter(x2, y2, color = ‘purple’)
plt.title('Scatter Plot')
plt.ylabel('Y Coordinate')
plt.xlabel('X Coordinate')
plt.legend(['Location 1’, ‘Location 2’])
plt.grid(False)
plt.show()
