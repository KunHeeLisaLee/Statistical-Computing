import numpy as np


def partition(list_to_be_sorted, p, r):
    """
    Input: list_to_be_sorted(list), p(start index), r(end index)
    Output: partition index
    """
    pivot_index = np.random.randint(p, r+1)  # updated: randomly pick pivot
    tmp = list_to_be_sorted[pivot_index]
    list_to_be_sorted[pivot_index] = list_to_be_sorted[r]
    list_to_be_sorted[r] = tmp

    x = list_to_be_sorted[r]  # set pivot
    i = p-1
    for j in range(p, r):
        if list_to_be_sorted[j] <= x:
            i = i+1
            tmp = list_to_be_sorted[i]
            list_to_be_sorted[i] = list_to_be_sorted[j]  # swap elements
            list_to_be_sorted[j] = tmp

    tmp = list_to_be_sorted[i+1]
    list_to_be_sorted[i+1] = list_to_be_sorted[r]
    list_to_be_sorted[r] = tmp  # move pivot to correct location

    return i+1


def quick_sort(list_to_be_sorted, p, r):
    """
    Input: list_to_be_sorted(list), p(start index), r(end index)
    Output: sorted list
    """
    if p < r:
        q = partition(list_to_be_sorted, p, r)
        quick_sort(list_to_be_sorted, p, q-1)
        quick_sort(list_to_be_sorted, q+1, r)

    return list_to_be_sorted


def apply_quick_sort(list_to_be_sorted):
    """
    Input: list_to_be_sorted(list)
    Output: sorted list
    """
    if not isinstance(list_to_be_sorted, list):
        raise TypeError("Input must be a list.")
    try:
        sorted(list_to_be_sorted)
    except TypeError:
        raise ValueError("Input must be a list of numbers.")
    quick_sort(list_to_be_sorted, 0, len(list_to_be_sorted)-1)
    return list_to_be_sorted
