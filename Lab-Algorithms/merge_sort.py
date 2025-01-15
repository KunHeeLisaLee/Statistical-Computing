def merge(list_to_be_sorted, start, mid, end):

    temp_list = [0]*(end-start+1)

    # Indexes for both intervals
    i = start
    j = mid + 1
    k = 0

    # Traverse both lists and in each iteration, add smaller of the elements
    # to the temp list
    while (i <= mid and j <= end):
        if (list_to_be_sorted[i] <= list_to_be_sorted[j]):
            temp_list[k] = list_to_be_sorted[i]
            k = k + 1
            i = i + 1
        else:
            temp_list[k] = list_to_be_sorted[j]
            k = k + 1
            j = j + 1

    # Add elements that are remaining in the first interval
    while (i <= mid):
        temp_list[k] = list_to_be_sorted[i]
        k = k + 1
        i = i + 1

    # Add elements that are remaining in the second interval
    while (j <= end):
        temp_list[k] = list_to_be_sorted[j]
        k = k + 1
        j = j + 1

    list_to_be_sorted[start:end+1] = temp_list


def apply_merge_sort(list_to_be_sorted, start, end):
    if (start < end):
        mid = int((start + end) / 2)
        apply_merge_sort(list_to_be_sorted, start, mid)
        apply_merge_sort(list_to_be_sorted, mid + 1, end)
        merge(list_to_be_sorted, start, mid, end)
        return list_to_be_sorted


def merge_sort(list_to_be_sorted):
    # Leaves the original list untouched
    list_to_be_sorted = list_to_be_sorted.copy()

    sorted_list = apply_merge_sort(list_to_be_sorted, 0,
                                   len(list_to_be_sorted)-1)
    return sorted_list
