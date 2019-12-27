"""
Author: Alejandro Sanchez Uribe
Date: 19 Dec 2019
"""

import random


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(list): Input array to search
       number(int): The target
    Returns:
       int: Index or -1
    """
    start = 0
    stop = len(input_list) - 1

    while start <= stop:
        # implement binary search
        midpoint = (start + stop) // 2

        if input_list[midpoint] == number:
            return midpoint

        # check if left side is sorted
        if input_list[start] <= input_list[midpoint]:
            # check if number is in range of the sorted left side
            if input_list[start] <= number < input_list[midpoint]:
                # continue search on left side
                stop = midpoint - 1
            else:
                # continue search on right side
                start = midpoint + 1

        # check if number is in range of sorted right side
        if input_list[midpoint] < number <= input_list[stop]:
            # continue search on right side
            start = midpoint + 1
        else:
            # continue search on left side
            stop = midpoint - 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]

    print(str(number) + ' @ ' + str(rotated_array_search(input_list, number)), end=': ')

    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Test Cases below:

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

test_function([[], 1])
test_function([[1], 1])
test_function([[1, 2], 2])
test_function([
    [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0,
     1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
     61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
    , random.randint(0, 99)])
