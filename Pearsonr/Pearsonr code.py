# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:21:00 2019

@author: swang
"""

'''
Compute Pearsonr
Note: Grains is an array of data 210 rows by 2 columns. 
'''

# Perform the necessary imports
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Assign the 0th column of grains: width
width = grains[:,0]

# Assign the 1st column of grains: length
length = grains[:,1]

# Scatter plot width vs length
plt.scatter(width, length)
plt.axis('equal')
plt.show()

# Calculate the Pearson correlation
correlation, pvalue = pearsonr(width,length)

# Display the correlation
print(correlation)
