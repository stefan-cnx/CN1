# Arguments are 'the values' that we pass into a function when calling the function.
# Parameters are 'the values' that the function requires to complete "the job".


# This function will take values into the function and return a list of multiple numbers as a result.
# Version 2
# :param number: value of the number that we want to find multiples off
# :param multiple: value of how many multiples we want to find
def multi_num(number, multiple):
    multi_num_list = []
    for i in range(multiple):
        new_multi_num = number * (i + 1)
        multi_num_list.append(new_multi_num)
    return multi_num_list  # "a list of the multiple numbers"
