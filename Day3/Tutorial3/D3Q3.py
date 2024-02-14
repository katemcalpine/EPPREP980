#--------------------------------------------------------------------
# Title: D3Q3.py
# Author: Kate McAlpine
# Email: kate.mcalpine@newcastle.edu.au
# Created: 14th February, 2024
# Found in: Day 3 Tutorial Slides
#--------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

def GradePlot(grades):
    plt.hist(grades)
    plt.title('Histogram')
    plt.ylabel('Frequency')
    plt.xlabel('Grades')
    plt.legend(['Grades Frequency'])
    plt.show()

# Read in CSV
data = pd.read_csv('ClassGrades.csv')

print(data.head())

# Isolate columns of data
grades = data['Grades'].values

GradePlot(grades)