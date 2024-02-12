#--------------------------------------------------------------------
# Title: ImportingCSV.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 25th November, 2023
# Found in: Day 3 Lecture Slides
#--------------------------------------------------------------------

import pandas as pd

# Read in CSV
data = pd.read_csv('CSVFile.csv')

print(data.head())

# Isolate columns of data
y = data['Height'].values
t = data['Time'].values

print (len(y), len(t))

print(y[3])
print(t[3])
