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