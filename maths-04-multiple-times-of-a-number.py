# A script that shows the first "multiple times" multiples of a number (number)
#                               ================           ====================
# The expected result is the numbers number times multiple, number times multiple, ...

# 1. Suggested Solution:
#=======================
print('\n1. Suggested Solution Result:') # To print a heading
print(  '=============================') # To print a heading underline
number = float(input('Enter a number to find multiples:'))
multiple = int(input('Enter the numbers of multiples to find:'))
for i in range(multiple):
    print(number * (i + 1))

"""
Above script will print to the console:

1. Suggested Solution Result:
=============================
1 times the value of the entered number (number), for 8 it would print 8
2 times the value of the entered number (number), for 8 it would print 16
continue as many times as the value of multiple
"""
