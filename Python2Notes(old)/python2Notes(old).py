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

#And Or Not
and, which checks if both the statements are True;
or, which checks if at least one of the statements is True;
not, which gives the opposite of the statement.