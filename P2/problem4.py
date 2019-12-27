"""
Author: Alejandro Sanchez Uribe
Date: 19 Dec 2019
"""


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_zero = 0
    next_two = len(input_list) - 1
    current = 0

    # the next_two variable denotes the point at which only 2s are present
    while current <= next_two:
        # save the value of the current item
        item = input_list[current]

        # if the edge values, 0 and 2, are sorted, the 1s are automatically sorted
        # so we start with the comparison to 0
        if item == 0:
            # if the value is a 0, it switches positions to the next index for consecutive 0s
            # for this we must place the value of next_zero at the current index
            input_list[current] = input_list[next_zero]
            #  and the current item, 0, at the next_zero index
            input_list[next_zero] = item
            # the index them moves on,
            # and takes note that the next_zero index already has a zero so it also moves forward
            next_zero += 1
            current += 1
        elif item == 2:
            # the same process is taken as with the 0s but at the end of the list
            input_list[current] = input_list[next_two]
            input_list[next_two] = item
            # therefore this value has to go down and approach the current index
            next_two -= 1
        else:
            # if the value is a 1 nothing must be done
            current += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Test Cases below:

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

test_function([])
test_function([1, 1, 1, 1, 1, 1])
test_function([0, 0, 0, 0, 0, 0])
test_function([2, 2, 2, 2, 2, 2])
test_function([0, 0, 0, 1, 1, 1])
test_function([0, 0, 0, 2, 2, 2])
test_function([1, 1, 1, 2, 2, 2])
