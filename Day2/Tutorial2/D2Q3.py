#--------------------------------------------------------------------
# Title: D2Q3.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 6th June, 2024
# Found in: Day 2 Tutorial Slides
#--------------------------------------------------------------------

import numpy as np

def sinApprox(x):
    sin = x - ((x**3)/(1*2*3)) + ((x**5)/(1*2*3*4*5)) - ((x**7)/(1*2*3*4*5*6*7)) + ((x**9)/(1*2*3*4*5*6*7*8*9)) - ((x**11)/(1*2*3*4*5*6*7*8*9*10*11)) + ((x**13)/(1*2*3*4*5*6*7*8*9*10*11*12*13)) - ((x**15)/(1*2*3*4*5*6*7*8*9*10*11*12*13*14*15))
    return sin

x = 5

print(sinApprox(x))

print(np.sin(5))
