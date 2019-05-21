'''
Quantiles are points that split a dataset into groups of equal size. 
For example, let’s say you just took a test and wanted to know whether you’re in the top 10% 
of the class. One way to determine this would be to split the data into 
ten groups with an equal number of datapoints in each group and see which group you fall into.

quartiles are some of the most commonly used quantiles. The quartiles split the data into four groups of equal size.
'''

# quantile() takes two parameters. The first is the dataset that you are using. The second parameter is a single number or a list of numbers between 0 and 1. 
# These numbers represent the places in the data where you want to split.
import numpy as np
dataset = [5, 10, -20, 42, -9, 10]
#split the first 10% of the data apart from the remaining 90%
ten_percent = np.quantile(dataset, 0.10)


from song_data import songs
import numpy as np
# Define twenty_third_percentile here:
#contains the value that splits the first 23% of the data from the rest of the data
twenty_third_percentile =  np.quantile(songs, 0.23)
#Ignore the code below here:
try:
  print("The value that splits 23% of the data is " + str(twenty_third_percentile) + "\n")
except NameError:
  print("You haven't defined twenty_third_percentile.")


# Many Quantiles
import numpy as np
dataset = [5, 10, -20, 42, -9, 10]
#four values that split the data into five groups of equal size
ten_percent = np.quantile(dataset, [0.2, 0.4, 0.6, 0.8])


from song_data import songs
import numpy as np
# Define quartiles, deciles, and tenth here:
#quartiles of a dataset split the data into four groups of equal size
quartiles = np.quantile(songs, [0.25, 0.5, 0.75])
#first value should be at 10% of the data. The next value should be at 20% of the data. The final value should be at 90% of the data.
deciles = np.quantile(songs,[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
#Ignore the code below here:
try:
  print("The quariles are " + str(quartiles) + "\n")
except NameError:
  print("You haven't defined quartiles.\n")
try:
  print("The deciles are " + str(deciles) + "\n")
except NameError:
  print("You haven't defined deciles.\n")


# 2-quantile. This value splits the data into two groups of equal size. 
#Half the data will be above this value, and half the data will be below it. This is also known as the median!

# 4-quantiles, aka quartiles, split the data into four groups of equal size

# percentiles, or the values that split the data into 100 groups, are commonly used to compare new data points to the dataset.
# percentiles are often used for IQ or statements like “You are above the 80th percentile in height”

from song_data import songs
import numpy as np
# 32nd percentile
percentile = np.quantile(songs, 0.32)
#Ignore the code below here:
try:
  print("Your percentile is " + str(percentile) + "\n")
except NameError:
  print("You haven't defined percentile")

'''
Quantiles are values that split a dataset into groups of equal size.
If you have n quantiles, the dataset will be split into n+1 groups of equal size.
The median is a quantile. It is the only 2-quantile. Half the data falls below 
the median and half falls above the median.
Quartiles and percentiles are other common quantiles. Quartiles split the data into 
4 groups while percentiles split the data into 100 groups.
'''