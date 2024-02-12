#--------------------------------------------------------------------
# Title: LineGraph2.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 25th November, 2023
# Found in: Day 3 Lecture Slides
#--------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

v0 = 5
g = 9.81
t = np.linspace(0, 1, 11)

y = v0*t – 0.5*g*t**2

plt.plot(t, y)
plt.plot(t, y, ‘o’)
plt.title(‘Line Graph')
plt.ylabel(‘Height')
plt.xlabel(‘Seconds')
plt.legend([‘Path'])
plt.grid(False)
plt.show()
