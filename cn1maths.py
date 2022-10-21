# Arguments are 'the values' that we pass into a function when calling the function.
# Parameters are 'the values' that the function requires to complete "the job".


def multi_num(number, multiple):
    """takes a number value and returns a list of multiple numbers
    
    :param number: value of the number that we want to find multiples off
    :type number: float
    :param multiple: value of how many multiples we want to find
    :type number: int
    
    :returns: list of multiple numbers
    :rtype: list
    
    >>>multi_num(3, 4)
    [3, 6, 9, 12]
    >>>multi_num(-3, 4)
    [-3, -6, -9, -12]
    
    STRATEGY: Use a for loop to multiply the number by i
    
    """
    multi_num_list = []
    for i in range(multiple):
        new_multi_num = number * (i + 1)
        multi_num_list.append(new_multi_num)
    return multi_num_list  # "a list of the multiple numbers"


def factors(number):
    """takes a whole number value and returns a list of found factors
    
    :param number: value of the number that we want to find the factors for
    :type number: int

    :returns: list of factors
    :rtype: list
    
    >>>factors(12)
    [1, 2, 3, 4, 6, 12]
    
    STRATEGY: Use a for loop and modulo (%) operator
    
    """
    factors_list = []
    factors_list.append(1)
    for i in range(int(number / 2), 1, -1):
        factor = number / i
        if number % i == 0:
            factor = int(factor)
            factors_list.append(factor)
    factors_list.append(number)
    return factors_list
