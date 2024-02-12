#--------------------------------------------------------------------
# Title: ExportingCSV.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 25th November, 2023
# Found in: Day 3 Lecture Slides
#--------------------------------------------------------------------

import numpy as np
import pandas as pd

v0 = 5
g = 9.81

# Initialise Arrays. Multidimensional arrays also work
t = np.linspace(0, 1, 1001)
y = v0*t-0.5*g*t**2

# Turn into Pandas DataFrame
time = pd.DataFrame({'Time': t})
height = pd.DataFrame({'Height': y})

# Concatenate DataFrames. 
# axis=1 stacks vertically, axis=0 stacks horizontally
data = pd.concat([time, height], axis=1)

# Export to CSV
data.to_csv('CSVFile.csv', index=False, header=True)
