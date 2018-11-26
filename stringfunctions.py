#String functions

myStr = 'HelloThereWorld1'

# Capitalize
print(myStr.capitalize())

# Swap case
print(myStr.swapcase())

# Get length (16 characters)
print(len(myStr))

# Replace
print(myStr.replace('World', 'Everyone'))

# Count
sub = "H"
print(myStr.count(sub))

# Startswith
print(myStr.startswith('Hello'))

# Endswith
print(myStr.endswith('!'))

# Split to list
print(myStr.split())

# find (location is 0)
print(myStr.find('H'))

# index (the index is 0)
print(myStr.index('H'))

#Is all alphanumeric
print(myStr.isalnum())

#Is all alphabetic
print(myStr.isalpha())

# Is all numeric
print(myStr.isnumeric())