#--------------------------------------------------------------------
# Title: NestedIfElifStatement.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 20th November, 2023
# Found in: Day 2 Lecture Slides
#--------------------------------------------------------------------

a = 5
b = 10
if (a == 5):
	b = 20
elif (a == 10):
	if (a < 5):
		b = 30
	elif (a > 5):
		b = 40
	print(a)
print(b)
