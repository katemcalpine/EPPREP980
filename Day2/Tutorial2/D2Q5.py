#--------------------------------------------------------------------
# Title: D2Q5.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 5th June, 2024
# Found in: Day 2 Tutorial Slides
#--------------------------------------------------------------------

x = 0
x1 = 1          # x-1
x2 = 0          # x-2

for i in range(0, 9):
        print(x)
        x = x1 + x2
        x1 = x2         # Shift values
        x2 = x          # Shift values
