"""
Author: Alejandro Sanchez Uribe
Date: 19 Dec 2019
"""


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # This function doesn't handle imaginary numbers so it stops here
    if number < 0:
        return None

    # Base cases:
    if number == 0 or number == 1:
        return number

    root = 1
    start = 1
    stop = number

    while start <= stop:
        # Find an initial search point: midpoint
        potential_root = (start + stop) // 2

        # Square and compare result to number
        result = potential_root ** 2
        # if the exact number, return number
        if result == number:
            return potential_root

        # if lower than the number, search new value
        if result < number:
            start = potential_root + 1
            root = potential_root

        # if higher than the number, search lower
        if result > number:
            stop = potential_root - 1

    return root


# Test Cases below:

print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

print("Pass" if (None is sqrt(-1)) else "Fail")
print("Pass" if (100 == sqrt(10000)) else "Fail")
print("Pass" if (1000 == sqrt(1000000)) else "Fail")
print("Pass" if (100 != sqrt(1000000)) else "Fail")
