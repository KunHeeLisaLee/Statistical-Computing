import numpy as np
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from selection_sort import selection_sort
from quick_sort import apply_quick_sort

# 1-1. Testing algorithms
list_1 = np.array([300, 943, 72, 202, 97, 216, 1])
print(bubble_sort(list_1))
print(merge_sort(list_1))
print(selection_sort(list_1))
print(apply_quick_sort(list_1))

list_2 = np.array([5, 4, 3, 6, 8])
print(bubble_sort(list_2))
print(merge_sort(list_2))
print(selection_sort(list_2))
print(apply_quick_sort(list_2))
