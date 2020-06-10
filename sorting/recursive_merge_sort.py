import sys
import random
from pydoc import locate


def sort(unsorted_list):
    """performs merge sort, calls split and merge

    Args:
        unsorted_list (list): original, unsorted list
    """
    split_unsorted_list = split(unsorted_list)
    return merge(split_unsorted_list)


def split(unsorted_list):
    """performs the split phase of merge sort, splits unsorted list into a list of lists, each of length 1

    Args:
        unsorted_list (list): the unsorted list, taken as input

    Returns:
        list: list of lists (e.g. [1, 2, 3, 4] => [[1], [2], [3], [4]])
    """
    return [[i] for i in unsorted_list]


def merge(split_unsorted_list):
    """performs the merge phase of merge sort, merges adjacent lists of sorted items until there exists only one list (the final sorted list)

    Args:
        split_unsorted_list (list): unsorted list of smaller sorted lists

    Returns:
        list: sorted list
    """
    if len(split_unsorted_list) <= 1:
        return split_unsorted_list[0]

    new_split_unsorted_list = []

    for i in range(0, len(split_unsorted_list), 2):
        split_1 = split_unsorted_list[i]
        try:
            split_2 = split_unsorted_list[i + 1]
        except IndexError:
            new_split_unsorted_list.append(split_1)
            break
        merged_list = []
        while len(split_1) + len(split_2) > 0:
            if len(split_1) == 0:
                merged_list += split_2
                break
            elif len(split_2) == 0:
                merged_list += split_1
                break
            if split_1[0] < split_2[0]:
                merged_list.append(split_1[0])
                split_1 = split_1[1:]
            else:
                merged_list.append(split_2[0])
                split_2 = split_2[1:]
        new_split_unsorted_list.append(merged_list)

    return merge(new_split_unsorted_list)


if __name__ == "__main__":
    """takes in a list of arguments"
    - First argument: name of file ('recursive_quicksort.py')
    - Second argument: list items type (e.g. 'int')
    - Third, fourth, fifth... argument: list items
    """
    item_type_constructor = locate(sys.argv[1])
    unsorted_list = [item_type_constructor(i) for i in sys.argv[2:]]
    print(sort(unsorted_list))
