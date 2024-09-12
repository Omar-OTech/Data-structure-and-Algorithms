def to_float_array(arr):
    return [int(i) if i.isnumeric() else float(i) for i in arr]

# 2nd solution
    # return [float(i) for i in arr]

# Test cases
print(to_float_array(["1.1", "2.2", "3.3"])) # [1.1, 2.2, 3.3]
print(to_float_array(["1", "2", "3"]))       # [1, 2, 3]
print(to_float_array(["1.1", "2", "3"]))     # [1.1, 2, 3]
print(to_float_array(["1", "2.2", "3"]))     # [1, 2.2, 3]