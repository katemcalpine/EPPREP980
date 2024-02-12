#--------------------------------------------------------------------
# Title: NestedIfElifElseStatement.py
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
	b = 30
else:
	if (a < 5):
		b = 40
	elif (a > 5):
		b = 50
	else:
		b = 60
	print(a)
print(b)
