"""
Author: Alejandro Sanchez Uribe
Date: 19 Dec 2019
"""
import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # prevent empty lists:
    if len(ints) < 1:
        return tuple((None, None))

    # values for comparison
    minimum = ints[0]
    maximum = ints[0]

    # since sorting is usually O(n log (n)), this will be iterated through without sorting
    # the list will only be traversed once, meaning this achieves O(n)
    for integer in ints:
        # each value is tested for highest value and lowest value status
        if integer < minimum:
            minimum = integer
        if integer > maximum:
            maximum = integer

    return tuple((minimum, maximum))


# Test Cases below:

# a list containing 0 - 9
lst = [i for i in range(0, 10)]
random.shuffle(lst)

print("Pass" if ((0, 9) == get_min_max(lst)) else "Fail")

# a list containing nothing
lst = []
random.shuffle(lst)
print("Pass" if ((None, None) == get_min_max(lst)) else "Fail")

# a list containing 0-100
lst = [i for i in range(0, 101)]
random.shuffle(lst)
print("Pass" if ((0, 100) == get_min_max(lst)) else "Fail")

# a list containing 0-999999
lst = [i for i in range(0, 1000000)]
random.shuffle(lst)
print("Pass" if ((0, 999999) == get_min_max(lst)) else "Fail")

# a list containing 0-999999 in reverse order, without shuffling
lst = [i for i in range(999999, -1, -1)]
print("Pass" if ((0, 999999) == get_min_max(lst)) else "Fail")