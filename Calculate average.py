def find_average(numbers):
# 1st solution
    res = 0
    if len(numbers) == 0:
        return 0
    for i in numbers:
        res += i
    return res / len(numbers)

# 2nd solution
    # return sum(numbers) / len(numbers) if numbers else 0



print(find_average([1, 2, 3])) # 2, "Failed for [1, 2, 3]"
print(find_average([])) # 0, "Failed for []"
print(find_average([1, 2, 3, 4])) # 2.5, "Failed for [1, 2, 3, 4]"
print(find_average([1, 2])) # 1.5, margin=1e-3, message="Failed for [1, 2]"
