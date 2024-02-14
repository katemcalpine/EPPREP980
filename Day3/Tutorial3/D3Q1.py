#--------------------------------------------------------------------
# Title: D3Q1.py
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
