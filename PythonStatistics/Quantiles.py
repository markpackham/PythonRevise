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