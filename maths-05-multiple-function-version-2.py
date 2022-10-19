# A script that shows the first "multiple times" multiples of a number (number)
#                               ================           ====================
# The script will be a reusable function!
#                      ========
# This is the second version with arguments and paramters:
# This function will take values into the function and return a list of multiple numbers as a result.
# Arguments are 'the values' that we pass into a function when calling the function.
# Parameters are 'the values' that the function requires to complete "the job".

def multi_num(number, multiple):
    multi_num_list = []
    for i in range(multiple):
        new_multi_num = number * (i + 1)
        multi_num_list.append(new_multi_num)
    return multi_num_list  # "a list of the multiple numbers"


# calling our new function:
print(multi_num(8, 4))

# calling our new function for a second time:
print(multi_num(4.5, 6))


