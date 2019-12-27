"""
Author: Alejandro Sanchez Uribe
Date: 19 Dec 2019
"""


def merge(left, right):
    merged = []
    left_i = 0
    right_i = 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            merged.append(left[left_i])
            left_i += 1
        else:
            merged.append(right[right_i])
            right_i += 1

    merged += left[left_i:]
    merged += right[right_i:]

    return merged


def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def rearrange_digits(items):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       items(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # if only one or less elements are in the list,
    # it is not necessary to move forward
    if len(items) <= 1:
        return items

    # sort with mergesort for O(n log(n))
    sorted_items = mergesort(items)
    # used to split the list into two numbers
    num_1_lst = []
    num_2_lst = []

    # iterate backwards to get higher values first
    for i in range(len(sorted_items) - 1, -1, -1):
        # place even index positioned values in one list,
        # starting with the highest value
        # appended as string to be able to use str join function later on
        if i % 2 == 0:
            num_1_lst.append(str(sorted_items[i]))
        # place odd index positioned values in the other list
        else:
            num_2_lst.append(str(sorted_items[i]))

    # join all values in the order they are in,
    # and convert to int
    num_1 = int(''.join(num_1_lst))
    num_2 = int(''.join(num_2_lst))

    return [num_1, num_2]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test Cases below:

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

test_function([[1, 1], [1, 1]])
test_function([[1], [1, 0]])
test_function([[], [0, 0]])
test_function([[11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1197531, 108642]])
test_function([[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [97531, 108642]])

