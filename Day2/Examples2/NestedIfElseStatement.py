#--------------------------------------------------------------------
# Title: NestedIfElseStatement.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 20th November, 2023
# Found in: Day 2 Lecture Slides
#--------------------------------------------------------------------

a = 5
b = 10
if (a == 5):
	b = 20
else:
	if (a < 5):
		b = 30
	else:
		b = 40
	print(a)
print(b)
