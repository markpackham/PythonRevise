#Python 2
print "Hello Python 2"
#Python 3
print("Hello Python 3")

#Following old Python 2
print "Hello " + "Me"

#float division
cucumbers = 100
num_people = 6
whole_cucumbers_per_person = cucumbers/num_people
print whole_cucumbers_per_person
float_cucumbers_per_person = float(cucumbers)/num_people
print float_cucumbers_per_person

#multi line string
haiku = """
The old pond,
A frog jumps in:
Plop!"""

#Boolean
age_is_12 = False
name_is_maria = True

#To String
float_1 = 0.25
float_2 = 40.0
product = float_1 * float_2
big_string = "The product was " + str(product)

#Escape character \
'This isn\'t flying, this is falling with style!'

#String methods
len()
lower()
upper()
str()

parrot = "Norwegian Blue"
print len(parrot)
parrot = "Norwegian Blue"
print parrot.lower()
parrot = "norwegian blue"
print parrot.upper()

#using %s (very simular to how C# works when taking the variable of a string which is cleaner than concatenating strings together)
string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)
#%d acts as a placeholder for a number but is used in a simlar manner to %s

#%s another example
name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")
print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)


Three ways to create strings
'Alpha'
"Bravo"
str(3)
String methods
len("Charlie")
"Delta".upper()
"Echo".lower()
Printing a string
print "Foxtrot"
Advanced printing techniques
g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h)


#Get datetime
from datetime import datetime
now = datetime.now()
print now

#Specific dates
from datetime import datetime
now = datetime.now()
print now.year
print now.month
print now.day

#Date formatting
from datetime import datetime
now = datetime.now()
print '%02d-%02d-%04d' % (now.month, now.day, now.year)
# will print the current date as mm-dd-yyyy

#Time formatting
from datetime import datetime
now = datetime.now()
print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

#And Or Not (works pretty much the same as other modern programming languages)
and, which checks if both the statements are True;
or, which checks if at least one of the statements is True;
not, which gives the opposite of the statement.

#If statement syntax
response = 'Y'
answer = "Left"
if answer == "Left":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"
# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.

#If Elif (Else If) Else
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

#Conditions
Comparators
3 < 4
5 >= 5
10 == 10
12 != 13
Boolean operators
True or False 
(3 < 4) and (5 >= 5)
this() and not that()
Conditional statements
if this_might_be_true():
  print "This really is true."
elif that_might_be_true():
  print "That is true."
else:
  print "None of the above."

#Long IF example
pyg = 'ay'
original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
    print 'empty'


#Function structure
def spam():
  """Prints 'Eggs!'"""
  print "Eggs!"
spam()

#Return Function
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared
square(10)

#Parameters & Arguments
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)
power(37, 4)  # Add your arguments here!

#import math
import math
print math.sqrt(25)


#Universal import can handle this for you. The syntax for this is:
from module import *

# Import *everything* from the math module
from math import *

#max
maximum = max(4, 8, 15)
print maximum

#min
minimum = min(4, 8, 15)
print minimum

#abs absolute
#abs() function returns the absolute value of the number it takes as an argument—that is, that number’s distance from 0 on an imagined number line. 
#For instance, 3 and -3 both have the same absolute value: 3. The abs() function always returns a positive value, 
#and unlike max() and min(), it only takes a single number.
absolute = abs(-42)
print absolute

#type reveals the variable type eg <type 'int'> <type 'float'> <type 'str'>
print type(108)
print type(3.14)
print type('hello')

#Function example, long
def hotel_cost(nights):
  return 140 * nights
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost
def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print trip_cost("Los Angeles", 5, 600)

#List aka Array
zoo_animals = ["pangolin", "cassowary", "sloth", "dog"];
if len(zoo_animals) > 3:
  print "The first animal at the zoo is the " + zoo_animals[0]
  print "The second animal at the zoo is the " + zoo_animals[1]
  print "The third animal at the zoo is the " + zoo_animals[2]
  print "The fourth animal at the zoo is the " + zoo_animals[3]

#List assign by Index
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
zoo_animals[2] = "hyena"
zoo_animals[3] = "lion"

#Append & List Length .append & len()
suitcase = [] 
suitcase.append("sunglasses")
suitcase.append("shirt")
suitcase.append("pants")
suitcase.append("shoes")
list_length = len(suitcase) # Set this to the length of suitcase
print "There are %d items in the suitcase." % (list_length)
print suitcase

#List Slicing (like getting a Substring)
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
# The first and second items (index zero and one)
first = suitcase[0:2]
# Third and fourth items (index two and three)
middle = suitcase[2:4]
# The last two items (index four and five)
last = suitcase[4:6]

#Remove items from List .remove()
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')

#Insert items into specific order of list
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")# Use index() to find "duck"
animals.insert(duck_index,"cobra")
print animals # Observe what prints after the insert operation

#For In loop
my_list = [1,9,3,8,5,7]
for number in my_list:
  print 2 * number

#.sort() array
start_list = [5, 3, 1, 2, 4]
square_list = []
for number in start_list:
  square_list.append(number ** 2)
square_list.sort()
print square_list
#[1, 4, 9, 16, 25]

#Dictionary (just a List with keys)
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print residents['Puffin'] # Prints Puffin's room number
print residents['Sloth']
print residents['Burmese Python']


# Dictionary add keys & values
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']
# Your code here: Add some dish-price pairs to menu!
menu['Hamburger'] = 8.50
menu['Pizza Slice'] = 3.50
menu['Salad'] = 10.00
print "There are " + str(len(menu)) + " items on the menu."
print menu


# del (delete stuff from Dictionaries, target the key)
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines
# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Plains Exhibit'
print zoo_animals


#Dictionary manipulation example
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50


#String Looping
for letter in "Codecademy":
  print letter 
# Empty lines to make the output pretty
print
print
word = "Programming is fun!"
for letter in word:
  # Only print out the letter i
  if letter == "i":
    print letter