#Conditional statements

x=4

#Basic If
if x < 6:
    print('This is true, x is less than 6')

#If Else
if x < 2:
    print('This is true')
else:
    print('This is false')

#Else If (stupidly named Elif)
color= 'red'

if color == 'yellow':
    print('Color is red')
elif color == 'blue':
    print('Color is blue')
else:
    print('Color is not red or blue')

#Nested if statements (not ideal when a logical operator will do the job)
color= 'red'
if color == 'red':
    if x <10:
        print('Color is red & x less than 10')

#Logical operators
if color == 'red' and x < 10:
    print('Color is red & x less than 10')