# A script that shows the first 4 multiples of 9
# The expected result is the numbers 9, 18, 27, 36

# 1. Suggested Solution:
#=======================
print('\n1. Suggested Solution Result:') # To print a heading
print(  '=============================') # To print a heading underline
print(9)
print(9 + 9)
print(9 + 9 + 9)
print(9 + 9 + 9 +9)

"""
Above script will print to the console:

1. Suggested Solution Result:
=============================
9
18
27
36
"""

# 2. Suggested Solution:
#=======================
print('\n2. Suggested Solution Result:') # To print a heading
print(  '=============================') # To print a heading underline
print(9 * 1)
print(9 * 2)
print(9 * 3)
print(9 * 4)

"""
Above script will print to the console:

2. Suggested Solution Result:
=============================
9
18
27
36
"""

# 3. Suggested Solution:
#=======================
print('\n3. Suggested Solution Result:') # To print a heading
print(  '=============================') # To print a heading underline
for i in range(4):
    print(9 * (i + 1))

"""
Above script will print to the console:

3. Suggested Solution Result:
=============================
9
18
27
36
"""
