"""
Author: Alejandro Sanchez Uribe
Date: 12 Dec 19
"""
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    output = []

    # check input validity:
    if suffix == '' or path == '':
        return 'Invalid suffix or path: Input was empty string'
    if not isinstance(suffix, str) or not isinstance(path, str):
        return 'Invalid suffix or path: Input was not of type str'

    # base case:
    if os.path.isfile(path):
        if path.endswith(suffix):
            output.append(path)
            return output

    # check if recursion required:
    if os.path.isdir(path):
        for sub_path in os.listdir(path):
            output.extend(find_files(suffix, os.path.join(path, sub_path)))

    return output


# test cases below:

found_files = find_files('.c', './testdir')
# finds: ./testdir/subdir1/a.c, ./testdir/subdir3/subsubdir1/b.c, ./testdir/subdir5/a.c, ./testdir/t1.c
print(found_files)

found_files = find_files('.c', './testdir/subdir1')
# finds: ./testdir/subdir1/a.c
print(found_files)

found_files = find_files('.c', './testdr')
# finds: nothing, since the file directory doesn't exist
print(found_files)

found_files = find_files('.c', '')
# returns warning of empty string
print(found_files)

found_files = find_files('.c', 0)
# returns warning of non string input
print(found_files)
