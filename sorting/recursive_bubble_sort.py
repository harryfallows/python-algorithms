import sys
import random
from pydoc import locate


def bubblesort(unsorted_list):
    """iterates over unsorted list, if the current item is greater than the next item they are swapped

    Args:
        unsorted_list (list): the unsorted list, taken as input

    Returns:
        list: sorted list (or sublist depending on the recursion depth)
    """
    changes = False

    for i in range(len(unsorted_list) - 1):
        if unsorted_list[i] > unsorted_list[i + 1]:
            temp = unsorted_list[i]
            unsorted_list[i] = unsorted_list[i + 1]
            unsorted_list[i + 1] = temp
            changes = True

    if changes:
        return bubblesort(unsorted_list)
    else:
        return unsorted_list


if __name__ == "__main__":
    """takes in a list of arguments"
    - First argument: name of file ('recursive_quicksort.py')
    - Second argument: list items type (e.g. 'int')
    - Third, fourth, fifth... argument: list items
    """
    item_type_constructor = locate(sys.argv[1])
    unsorted_list = [item_type_constructor(i) for i in sys.argv[2:]]
    print(bubblesort(unsorted_list))
