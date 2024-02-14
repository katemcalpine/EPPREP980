#--------------------------------------------------------------------
# Title: D2Q1.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 14th February, 2024
# Found in: Day 2 Tutorial Slides
#--------------------------------------------------------------------

item = 0
orange = 2
strawberry = 0.5
total = 0

f = int(input('How many oranges? '))
total = orange * f
item = item + f

f = int(input('How many strawberries? '))
total = total + (strawberry * f)
item = item + f

if (item >= 5):
    total = total * 0.9

print(total)
