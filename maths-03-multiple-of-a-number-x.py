# A script that shows the first 4 multiples of a number (x)
#                                           ===============
# The expected result is the numbers x times 1, x times 2, x times 3, x times 4

# 1. Suggested Solution:
#=======================
print('\n1. Suggested Solution Result:') # To print a heading
print(  '=============================') # To print a heading underline
x = 8
print(x * 1)
print(x * 2)
print(x * 3)
print(x * 4)

"""
Above script will print to the console:

1. Suggested Solution Result:
=============================
8
16
24
32
"""

# 2. Suggested Solution:
#=======================
print('\n2. Suggested Solution Result:') # To print a heading
print(  '=============================') # To print a heading underline
x = 8
for i in range(4):
    print(x * (i + 1))
"""
Above script will print to the console:

2. Suggested Solution Result:
=============================
8
16
24
32
"""

# 3. Suggested Solution:
#=======================
print('\n3. Suggested Solution Result:') # To print a heading
print(  '=============================') # To print a heading underline
x = input('Please enter a number:')  # this will ask user to enter a string
x = float(x) # this will convert the string value to an float value
for i in range(4):
    print(x * (i + 1))
"""
Above script will print to the console:

3. Suggested Solution Result:
=============================
1 times the value of the entered number, for 8 it would print 8
2 times the value of the entered number, for 8 it would print 16
3 times the value of the entered number, for 8 it would print 24
4 times the value of the entered number, for 8 it would print 36
"""
