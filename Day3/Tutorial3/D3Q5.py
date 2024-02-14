#--------------------------------------------------------------------
# Title: D3Q5.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 14th February, 2024
# Found in: Day 3 Tutorial Slides
#--------------------------------------------------------------------

import pandas as pd

# Read in CSV
data = pd.read_csv('ClassGrades.csv')

print(data.head())

# Isolate columns of data
grades = data['Grades'].values

HDcount = 0
Dcount = 0
Ccount = 0
Pcount = 0

HDave = 0
Dave = 0
Cave = 0
Pave = 0

for i in range(0, len(grades)):
    if (grades[i] >= 85):
        HDcount = HDcount + 1
        HDave = HDave + grades[i]
    elif ((grades[i] >= 75) and (grades[i] < 85)):
        Dcount = Dcount + 1
        Dave = Dave + grades[i]
    elif ((grades[i] >= 65) and (grades[i] < 75)):
        Ccount = Ccount + 1
        Cave = Cave + grades[i]
    else: # Anything between 50 and 64
        Pcount = Pcount + 1
        Pave = Pave + grades[i]

print('HD count:', HDcount, '\nD count:', Dcount, '\nC count:', Ccount, '\nP count:', Pcount)
print('HD average:', HDave/HDcount, '\nD average:', Dave/Dcount, '\nC average:', Cave/Ccount, '\nP average:', Pave/Pcount)