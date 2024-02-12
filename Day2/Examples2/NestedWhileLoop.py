#--------------------------------------------------------------------
# Title: NestedWhileLoop.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 20th November, 2023
# Found in: Day 2 Lecture Slides
#--------------------------------------------------------------------

a = 5
b = 10
while (a <= 10):
	while (b <= 20):
		b = b + 2
	a = a + 1
print(a, b)
