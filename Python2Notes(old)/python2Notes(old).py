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

#.join()
#Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

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
#The default starting index is 0.
#The default ending index is the end of the list.
#The default stride is 1.
my_list = range(1, 11) # List of numbers 1 - 10
print my_list[::2]
#gives [1, 3, 5, 7, 9]
#Reverse List uses a negative stride
letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]
#['E', 'D', 'C', 'B', 'A']

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


#range() function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.
range(6) # => [0, 1, 2, 3, 4, 5]
range(1, 6) # => [1, 2, 3, 4, 5]
range(1, 6, 3) # => [1, 4]
The range function has three different versions:
range(stop)
range(start, stop)
range(start, stop, step)
In all cases, the range() function returns a list of numbers from start up to (but not including) stop. Each item increases by step.
If omitted, start defaults to 0 and step defaults to 1.

#range iteration example
n = [3, 5, 7]
def total(numbers):
  result = 0
  for i in range(0,len(numbers)):
    result += numbers[i]
  return result

#join 2 lists
m = [1, 2, 3]
n = [4, 5, 6]
def join_lists(x, y):
	return x + y
print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]


#multi dimensional list
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results
print flatten(n)


#While loop
count = 0
if count < 5:
  print "Hello, I am an if statement and count is", count
while count < 10:
  print "Hello, I am a while and count is", count
  count += 1


#Break
count = 0
while True:
  print count
  count += 1
  if count >= 10:
    break

#random (random numbers) & break
import random
print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"
count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"


#For In Range
print "Counting..."
for i in range(20):
  print i


#Modulous % / is even
def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
print is_even(5)
print is_even(6)


#Prime number check example
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True
print is_prime(13)
print is_prime(10)


#factorial
#factorial(4) would equal 4 * 3 * 2 * 1, which is 24.
def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total


#reverse
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
print reverse("Hello World")


#anti vowel
def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
          if char not in vowels:
            result += char
    return result
print anti_vowel("hello book")


#remove duplicates
def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    # Sort the input list from low to high    
    inputlist = sorted(inputlist)
    # Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]
    # Go through the values of the sorted list and append to the output list
    # ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
    return outputlist
print remove_duplicates([1, 1, 2, 2])


#median
def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
print median([2, 4, 5, 9])


#.items() method is used to return the list with all dictionary keys with values.
#.items() returns an array of tuples, a tuple is an unchangeable list
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}
print my_dict.items()
#[('age', 31), ('name', 'Nick'), ('occupation', 'Dentist')]


#Dictionary keys & values
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}
print my_dict.keys()
print my_dict.values()

#Dictionary Loop In
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}
for key in my_dict:
  print key, my_dict[key]

#lambda creates is an anonymous function
lambda x: x % 3 == 0
#Is the same as
def by_three(x):
  return x % 3 == 0
#If you plan on creating a function you’ll use over and over, you’re better off using def and giving that function a name

#Bitwise operations are operations that directly manipulate bits
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT


# bin() convert number to binary
print bin(1)
print bin(2)
print bin(3)
print bin(4)
print bin(5)
"""
0b1
0b10
0b11
0b100
0b101
"""

# int() function that you’ve seen a bit of already. It can turn non-integer input into an integer
#int function actually has an optional second parameter.
int("110", 2)
#gives 6
#When given a string containing a number and the base that number is in, the function will return the value of that number converted to base ten.

#Class example
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age
hippo = Animal('Anderson', 36)
sloth = Animal('Dale', 15)
ocelot = Animal('Fuzzy', 7)
print hippo.health
print sloth.health
print ocelot.health


#Inheritance (Triangle steals abilities of Shape)
class Shape(object):
  """Makes shapes!"""
  #__init__() as the method that “boots up” a class’ instance object: the init bit is short for “initialize.” (a constructor)
  def __init__(self, number_of_sides):
    #refer to the instance object called "self" , self is "this"
    #unlike "this" in other languages you have to include self explicitly as first parameter to an instance method in Python
    self.number_of_sides = number_of_sides
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3

#Override class one is inheriting from
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00

#Class Example
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))    
  def drive_car(self):
    self.condition = "used"   
class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type
    
  def drive_car(self):
    self.condition = "like new"
my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition


#open() file with read & write
my_file = open("output.txt", "r+")
#write-only mode ("w")
#read-only mode ("r")
#read and write mode ("r+")
#append mode ("a"), which adds any new data you write to the file to the end of the file.


#write file using .write()
my_list = [i ** 2 for i in range(1, 11)]
my_file = open("output.txt", "w")
# Add your code below!
for value in my_list:
  my_file.write(str(value) + "\n")
my_file.close()

#read file via .read()
my_file = open("output.txt", "r")
print my_file.read()
my_file.close()

#read specific line via .readline()
my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

#CLOSE after doing IO, stop wasting memory use .close()
#If you write to a file without closing, the data won’t make it to the target file.

#with & as
#use "with" if you're too lazy to bother with .close()
with open("text.txt", "w") as my_file:
  my_file.write("My Data!")

#closed - use .closed() to check if a file is closed
#.closed() says True when the file is closed and False otherwise
with open("text.txt", "w") as my_file:
  my_file.write("My Data!")
if not file.closed:
  file.close()
print my_file.closed