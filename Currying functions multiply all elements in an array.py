def multiply_all(arr):
    return lambda x: [i * x for i in arr]



print(type(multiply_all([1])(1))==list, True)
print(len(multiply_all([1, 2])(1)))    # 2, "array should have the same length as the array passed in as an argument")
print(multiply_all([1, 2, 3])(1))      # [1, 2, 3])
print(multiply_all([1, 2, 3])(2))      # [2, 4, 6])
print(multiply_all([1, 2, 3])(0))      # [0, 0, 0])
print(multiply_all([])(10))            # [], "should return an empty array")