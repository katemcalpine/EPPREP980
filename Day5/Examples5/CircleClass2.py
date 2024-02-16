#--------------------------------------------------------------------
# Title: CircleClass2.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 5th December, 2023
# Found in: Day 5 Lecture Slides
#--------------------------------------------------------------------

import numpy as np

class Circle:
    def __init__(self, radius):
        self.r = radius

    def area(self):
        a = np.pi * self.r**2
        print(a)

    def circumference(self):
        c = 2 * np.pi * self.r
        print(c)