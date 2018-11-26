#Variables & Data Types
greeting = 'Hello World'
greeting = 'Hello Planet'

#reassing the variable to the last one
print(greeting)

#Data Types
myStr = 'Hello'
myInt = 25
myFloat = 1.4

myList = [1,2,3,'A list is a 1D array']
myDict = {'aKey':'aValue','bKey':'bValue'}

#<class 'str'> Hello
print(type(myStr),myStr);
print(type(myInt),myInt);
print(type(myFloat),myFloat);
print(type(myList),myList);
print(type(myDict),myDict);

print(myList[3])
print(myDict['aKey'])

print(myStr,'-add this to the variable')
greeting = myStr + ' add this'
print(greeting)