def sort_array(source_array):
    odd_numbers = sorted([i for i in source_array if i % 2 != 0])
    print(odd_numbers)
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odd_numbers.pop(0)
    return source_array



print(sort_array([5, 3, 2, 8, 1, 4]))                 # [1, 3, 2, 8, 5, 4]
print(sort_array([5, 3, 1, 8, 0]))                    # [1, 3, 5, 8, 0]
print(sort_array([]))                                 # []
print(sort_array([5, 3, 2, 8, 1, 4, 11]))             # [1, 3, 2, 8, 5, 4, 11]
print(sort_array([2, 22, 37, 11, 4, 1, 5, 0]))        # [2, 22, 1, 5, 4, 11, 37, 0]
print(sort_array([1, 111, 11, 11, 2, 1, 5, 0]))       # [1, 1, 5, 11, 2, 11, 111, 0]
print(sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sort_array([0, 1, 2, 3, 4, 9, 8, 7, 6, 5]))     # [0, 1, 2, 3, 4, 5, 8, 7, 6, 9]