def selection_sort(list_to_be_sorted):
    # Leaves the original list untouched
    list_to_be_sorted = list_to_be_sorted.copy()

    # Traverse through all array elements
    for i in range(len(list_to_be_sorted)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(list_to_be_sorted)):
            if list_to_be_sorted[min_idx] > list_to_be_sorted[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        tmp = list_to_be_sorted[i]
        list_to_be_sorted[i] = list_to_be_sorted[min_idx]
        list_to_be_sorted[min_idx] = tmp

    return list_to_be_sorted
