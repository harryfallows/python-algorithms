import sys
import random
from pydoc import locate


def sort(unsorted_list):
    """recursively splits the unsorted list until each sublist is of length 1, then 'merges' these splits and returns a sorted list

    Args:
        unsorted_list (list): the unsorted list, taken as input

    Returns:
        list: the sorted list
    """
    if len(unsorted_list) <= 1:
        return unsorted_list
    split_point = len(unsorted_list) // 2
    return merge(sort(unsorted_list[:split_point]), sort(unsorted_list[split_point:]))


def merge(split_1, split_2):
    """performs the merge phase of merge sort, takes two sorted lists and returns one sorted list

    Args:
        split_1 (list): sorted list
        split_2 (list): sorted list

    Returns:
        list: sorted list
    """
    merged_list = []
    while len(split_1) != 0 and len(split_2) != 0:
        if split_1[0] < split_2[0]:
            merged_list.append(split_1[0])
            split_1 = split_1[1:]
        else:
            merged_list.append(split_2[0])
            split_2 = split_2[1:]
    merged_list += split_1
    merged_list += split_2

    return merged_list


if __name__ == "__main__":
    """takes in a list of arguments"
    - First argument: name of file ('recursive_quicksort.py')
    - Second argument: list items type (e.g. 'int')
    - Third, fourth, fifth... argument: list items
    """
    item_type_constructor = locate(sys.argv[1])
    unsorted_list = [item_type_constructor(i) for i in sys.argv[2:]]
    print(sort(unsorted_list))
