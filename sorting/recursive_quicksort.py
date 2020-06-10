import sys
import random
from pydoc import locate


def quicksort(unsorted_list):
    """main driver code for the quicksort algorithm:
    1. checks if the list contains 1 or 0 items, if it does the list is already sorted so it is returned
    2. chooses a random pivot in the unsorted list
    3. removes the pivot value from the unsorted list
    calls the partition function on the new unsorted list and pivot value
    4. returns the concatenation of the sorted left partition, the list containing the pivot, and the sorted right partition

    Args:
        unsorted_list (list): the unsorted list, taken as input

    Returns:
        list: sorted list (or sublist depending on the recursion depth)
    """
    if len(unsorted_list) <= 1:
        return unsorted_list
    pivot_idx = random.choice(range(len(unsorted_list)))
    pivot = unsorted_list[pivot_idx]
    new_unsorted_list = unsorted_list[:pivot_idx] + unsorted_list[pivot_idx + 1 :]
    l, r = partition(new_unsorted_list, pivot)
    return quicksort(l) + [pivot] + quicksort(r)


def partition(list_to_partition, pivot):
    """splits the unsorted list into two lists, one with the values less than the pivot, and another with the values greater than or equal to the pivot

    Args:
        list_to_partition (list): unsorted list portion
        pivot (type of list items): chosen sorting pivot for the current iteration

    Returns:
        tuple: (left partition, right partition)
    """
    l = [i for i in list_to_partition if i < pivot]
    r = [i for i in list_to_partition if i >= pivot]
    return l, r


if __name__ == "__main__":
    """takes in a list of arguments"
    - First argument: name of file ('recursive_quicksort.py')
    - Second argument: list items type (e.g. 'int')
    - Third, fourth, fifth... argument: list items
    """
    item_type_constructor = locate(sys.argv[1])
    unsorted_list = [item_type_constructor(i) for i in sys.argv[2:]]
    print(quicksort(unsorted_list))
