# A script that shows the first "multiple times" multiples of a number (number)
#                               ================           ====================
# The script will be a reusable function!
#                      ========

def multi_num():
    number = float(input('Enter a number to find multiples:'))
    multiple = int(input('Enter the numbers of multiples to find:'))
    for i in range(multiple):
        print(number * (i + 1))
    return

# calling our new function:
multi_num()

# calling our new function for a second time:
multi_num()
