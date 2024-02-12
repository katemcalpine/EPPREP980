#--------------------------------------------------------------------
# Title: NestedForLoop.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 20th November, 2023
# Found in: Day 2 Lecture Slides
#--------------------------------------------------------------------

a = 5
b = 10
for i in range(0, 10, 2)
	for j in range(0, 10, 2)
		b = b + 2
	a = a + 1
print(a, b)
