def bubble_sort(list_to_be_sorted):
    # Leaves the original list untouched
    list_to_be_sorted = list_to_be_sorted.copy()

    n = len(list_to_be_sorted)

    # Traverse through all array elements
    for i in range(n-1):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1,
            # swap if the element found is greater
            # than the next element
            if list_to_be_sorted[j] > list_to_be_sorted[j+1]:
                tmp = list_to_be_sorted[j]
                list_to_be_sorted[j] = list_to_be_sorted[j+1]
                list_to_be_sorted[j+1] = tmp

    return list_to_be_sorted
