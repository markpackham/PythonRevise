# Whiskers of a boxplot display information related to the spead of the dataset.
'''
There are many different ways to plot the whiskers of a boxplot. 
You might see some boxplots where the whiskers extend to the minimum and maximum values. 
Some boxplots have whiskers that extend one standard deviation away from the mean of the data.

However, one of the most commonly used methods of drawing the whiskers is to extend them 1.5 
times the interquartile range from the first and third quartile.

 An outlier is a point in the dataset that falls outside of the whiskers
 Outliers are usually represented with a dot or an asterisk.
'''

# matplotlib.pyplot module has a function named boxplot(). 
# boxplot() takes a dataset as a parameter. 
# This dataset could be something like a list of numbers, or a Pandas DataFrame.
# One of the strengths of Matplotlib is the ease of plotting multiple boxplots side by side
import codecademylib3_seaborn
import matplotlib.pyplot as plt
from music_data import two_thousand, two_thousand_one, two_thousand_two
plt.boxplot([two_thousand, two_thousand_one, two_thousand_two], labels = ["2000 Songs", "2001 Songs", "2002 Songs"])
plt.show()

'''
The box of a boxplot visualizes the median, first quartile, and third quartile of a dataset.
The length of the box in a boxplot visualizes the interquartile range.
The whiskers extend from the box 1.5 times the size of the interquartile range.
Outliers are points that fall outside of the whiskers. They’re represented by dots.
Boxplots are especially useful for comparing the spread of multiple datasets.
'''