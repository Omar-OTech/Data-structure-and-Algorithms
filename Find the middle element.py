def gimme(input_array):
# ist solution
    res = 0
    for i in range(3):
        if input_array[i] != max(input_array) and input_array[i] != min(input_array):
            res = i
    return res

# 2nd solution
    # return input_array.index(sorted(input_array)[1])

print(gimme([2, 3, 1]))    # 0, 'Finds the index of middle element'
print(gimme([5, 10, 14]))  # 1, 'Finds the index of middle element'