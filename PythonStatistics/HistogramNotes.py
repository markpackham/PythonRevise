﻿#Histograms are helpful for understanding how your data is distributed. While the average time a customer 
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