# Mean/Average
#np.average()
# Import packages
import numpy as np
import pandas as pd
# Read author data
greatest_books = pd.read_csv("top-hundred-books.csv")
# Set author ages to a NumPy array
author_ages = greatest_books['Ages']
# Use numpy to calculate the average age of the top 100 authors
average_age = np.average(author_ages)
print("The average age of the 100 greatest authors, according to a survey by Le Monde, is: " + str(average_age))


# Median np.median()
# Import packages
import numpy as np
import pandas as pd
# Read in author data
greatest_books = pd.read_csv("top-hundred-books.csv")
# Save author ages to author_ages
author_ages = greatest_books['Ages']
# Use numpy to calculate the median age of the top 100 authors
median_age = np.median(author_ages)
print("The median age of the 100 greatest authors, according to a survey by Le Monde is: " + str(median_age))


# Mode/Most common stats.mode()
# Import packages
import numpy as np
import pandas as pd
from scipy import stats
# Read in author data
greatest_books = pd.read_csv("top-hundred-books.csv")
# Save author ages to author_ages
author_ages = greatest_books['Ages']
# Use numpy to calculate the median age of the top 100 authors
mode_age = stats.mode(author_ages)
print("The mode age and its frequency of authors from Le Monde's 100 greatest books is: " + str(mode_age[0][0]) + " and " + str(mode_age[1][0]))

#Variance can mess things off if you have some out of the norm data sets
#eg a teacher could focus on 1 pupil to get them to have super high grades to boost the class average score whilst neglecting many others
#Distance from the mean, difference=X−μ
#Where X is a single data point and the Greek letter mu is the mean.
#Square the value so Negative numbers don't mess things up difference= (X - \mu)^2 
import numpy as np
grades = [88, 82, 85, 84, 90]
mean = np.mean(grades)
#When calculating these variables, square the difference.
difference_one = (88 - mean)** 2
difference_two = (82 - mean)** 2
difference_three = (85 - mean)** 2
difference_four = (84 - mean)** 2
difference_five = (90 - mean)** 2
difference_sum = difference_one + difference_two + difference_three + difference_four + difference_five
variance = difference_sum / 5
print("The sum of the squared differences is " + str(difference_sum))
print("The variance is " + str(variance))


#var() function takes a list of numbers as a parameter and returns the variance of that dataset.
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
teacher_one_grades = [80.24, 81.15, 81.29, 82.12, 82.52, 82.54, 82.76, 83.37, 83.42, 83.45, 83.47, 83.79, 83.91, 83.98, 84.03, 84.69, 84.74, 84.89, 84.95, 84.95, 85.02, 85.18, 85.53, 86.29, 86.83, 87.29, 87.47, 87.62, 88.04, 88.5]
teacher_two_grades = [65.82, 70.77, 71.46, 73.63, 74.62, 76.53, 76.86, 77.06, 78.46, 79.81, 80.64, 81.61, 81.84, 83.67, 84.44, 84.73, 84.74, 85.15, 86.55, 88.06, 88.53, 90.12, 91.27, 91.62, 92.86, 94.37, 95.64, 95.99, 97.69, 104.4]
#Set these two variables equal to the variance of each dataset using NumPy
teacher_one_variance = np.var(teacher_one_grades)
teacher_two_variance = np.var(teacher_two_grades)
print("The mean of the test scores in teacher one's class is " + str(np.mean(teacher_one_grades)))
print("The mean of the test scores in teacher two's class is " + str(np.mean(teacher_two_grades)))
print("The variance of the test scores in teacher one's class is " +str(teacher_one_variance))
print("The variance of the test scores in teacher two's class is " +str(teacher_two_variance))


#std() takes a dataset as a parameter and returns the standard deviation of that dataset
#a quantity expressing by how much the members of a group differ from the mean value for the group like varience but uses **0.5 squaring
#By taking the square root of the variance, the standard deviation gives 
#you a statistic about spread that can be easily interpreted and compared to the mean.
import numpy as np
from data import nba_data, okcupid_data
#Change these variables to be the standard deviation of each dataset. Use NumPy's function!
nba_standard_deviation = np.std(nba_data)
okcupid_standard_deviation = np.std(okcupid_data)
#IGNORE CODE BELOW HERE
print("The standard deviation of the NBA dataset is " +str(nba_standard_deviation))
print("The standard deviation of the OkCupid dataset is " + str(okcupid_standard_deviation))
