# Open a file that already exists
# "w" means you are going to write to the file
fo = open('test.txt', 'w')
# Get some info
print('Name: ', fo.name)
#Is the file opened or closed in our script?
print('Is Closed: ', fo.closed)
#Should say that it is in "w" ergo writing mode
print('Opening Mode: ', fo.mode)
# Write to file
fo.write('I love Python')
fo.write(' and JavaScript')
# Close file
fo.close()

# Open to append, "a" is for append mode
fo = open('test.txt', 'a')
fo.write(' I also like PHP')
fo.close()

# Read from file
fo = open('test.txt', 'r+')
text = fo.read(10)
print(text)
fo.close()

# Create file
fo = open('test2.txt', 'w+')
fo.write('This is my new file')
fo.close()