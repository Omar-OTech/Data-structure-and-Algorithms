def merge_arrays(first, second):
    return sorted(set(first + second))


print(merge_arrays([1, 3, 5], [2, 4, 6]))  #  [1, 2, 3, 4, 5, 6]
print(merge_arrays([2, 4, 8], [2, 4, 6]))  #  [2, 4, 6, 8]