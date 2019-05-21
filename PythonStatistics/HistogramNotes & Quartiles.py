#Histograms are helpful for understanding how your data is distributed. While the average time a customer 
#may arrive at the grocery store is 3 pm, the manager knows 3 pm is not the busiest time of day.

#range of your data is the difference between the maximum value and the minimum value in your dataset.
#range = max(data)\ -\ min(data)range=max(data) − min(data)

# Import packages
import numpy as np
import pandas as pd
# Read in transactions data
transactions = pd.read_csv("transactions.csv")
# Save transaction data to numpy arrays
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values
# Find the minimum time, maximum time, and range
min_time = np.amin(times)
max_time = np.amax(times)
range_time = max_time - min_time
# Printing the values
print("Earliest Time: " + str(min_time))
print("Latest Time: " + str(max_time))
print("Time Range: " + str(range_time))

#bin is a sub-range of values that falls within the range of a dataset.
#In a grocery store example, a valid bin may be from 0 hours to 6 hours.
# Import packages
import numpy as np
import pandas as pd
# Array of days old bread
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])
# Set the minimum and maximums of the array below
min_days_old = 0
max_days_old = np.max(days_old_bread)
# Set the number of bins to 3
bins = 3
# Calculate the bin range
try:
	bin_range = (max_days_old - min_days_old + 1) / bins
	print("Bins: " + str(bins))
	print("Bin Width: " + str(bin_range))
# Printing the values
except:
	print("You have not set the min, max, or bins values yet.")


#count is the number of values that fall within a bin’s range. For example, if 100 customers arrive at your 
#grocery store between midnight (0) and 6 am (6), your count for that bin is equal to 100.
# Import packages
import numpy as np
import pandas as pd
# Array of days old bread
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])
# Count the values in each bin 
days_old_012 = 4
days_old_345 = 2
days_old_678 = 4
# Printing the values
print("Between 0 and 2 days: " + str(days_old_012))
print("Between 3 and 5 days: " + str(days_old_345))
print("Between 6 and 8 days: " + str(days_old_678))


#numpy.histogram() is a faster way to count the number of values in a bin
#CAREFUL, it's like a Loop, mess up & it may run forever
# Import packages
import numpy as np
import pandas as pd
# Read in transactions data
transactions = pd.read_csv("transactions.csv")
# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values
# Use numpy.histogram() below
times_hist = np.histogram(times, range = (0, 24), bins = 4)
print(times_hist)
#Gives (array([101, 231, 213, 455]), array([  0.,   6.,  12.,  18.,  24.]))


# Histogram example, use from matplotlib import pyplot as plt
# Import packages
import codecademylib
import numpy as np
import pandas as pd
# import pyplot as plt
from matplotlib import pyplot as plt
# Read in transactions data
transactions = pd.read_csv("transactions.csv")
# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values
# Use plt.hist() below
plt.hist(times, range = (0, 24), bins = 4, edgecolor='black')
plt.title("Weekday Frequency of Customers")
plt.xlabel("Hours (1 hour increments)")
plt.ylabel("Count")
plt.show()

# Histogram is calculated via NumPy or plotted with Matplotlib.

# Skew
'''Once you have the center and range of your data, you can begin to describe its shape. 
The skew of a dataset is a description of the data’s symmetry.
A dataset with one prominent peak, and similar tails to the left and right is called symmetric. 
The median and mean of a symmetric dataset are similar.

A histogram with one prominent peak to the right, and a tail that extends to the left is called a left-skewed dataset.
'''

# modality describes the number of peaks in a dataset. 
# datasets with one distinct peak, known as unimodal. This is the most common.
# bimodal dataset has two distinct peaks.
# multimodal dataset has more than two peaks
# datasets with no obvious clustering. Datasets such as these are called uniform distributions

# Outliers
# If you see an outlier in your dataset, it’s worth reporting and investigating. 
# This data can often indicate an error in your data or an interesting insight.


# Quartiles
# A common way to communicate a high-level overview of a dataset is to find the values that split the data into four groups of equal size.
# By doing this, we can then say whether a new datapoint falls in the first, second, third, or fourth quarter of the data.
# quantile() function takes two parameters. The first is the dataset you’re interested in. The second is a number between 0 and 1.
import numpy as np
dataset = [50, 10, 4, -3, 4, -20, 2]
#calculates the third quartile of the given dataset
third_quartile = np.quantile(dataset, 0.75)



from song_data import songs
import numpy as np
#Create the variables songs_q1, songs_q2, and songs_q3 here:
songs_q1 = np.quantile(songs,0.25)
songs_q2 = np.quantile(songs,0.50)
songs_q3 = np.quantile(songs,0.75)
favorite_song = 120
quarter = 1
#Ignore the code below here:
try:
  print("The first quartile of dataset one is " + str(songs_q1) + " seconds")
except NameError:
  print("You haven't defined songs_q1")
try:
  print("The second quartile of dataset one is " + str(songs_q2)+ " seconds")
except NameError:
  print("You haven't defined songs_q2")
try:
  print("The third quartile of dataset one is " + str(songs_q3)+ " seconds")
except NameError:
  print("You haven't defined songs_q3\n")

'''
Buisnesses might compare their revenue to other companies by looking at quartiles (where I heard of the word before).
In fact quartiles are so commonly used that the three quartiles, along with the minimum and the maximum values of 
a dataset, are called the five-number summary of the dataset. 
These five numbers help you quickly get a sense of the range, centrality, and spread of the dataset.
'''


# IQR interquartile range is the difference between the third quartile (Q3) and the first quartile (Q1)
# iqr() function takes a dataset as a parameter and returns the Interquartile Range. 
# Notice that when we imported iqr(), we imported it from the stats submodule
# IQR is that it is a statistic, like the range, that helps describe the spread of the center of the data.
# unlike the range, the IQR is robust. A statistic is robust when outliers have little impact on it. 
from scipy.stats import iqr
dataset = [4, 10, 38, 85, 193]
interquartile_range = iqr(dataset)


from song_data import songs
from scipy.stats import iqr
#Create the variables interquartile_range here:
interquartile_range = iqr(songs)
# Ignore the code below here
try:
  print("The IQR of the dataset is " + str(interquartile_range) + "\n")
except NameError:
  print("You haven't defined interquartile_range yet\n")


