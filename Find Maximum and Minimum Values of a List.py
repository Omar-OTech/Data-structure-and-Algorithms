def minimum(arr):
# 1st solution
    return min(arr)

# 2nd solution
    # return sorted(arr)[0]

# 3rd solution
    # min_num = arr[0]
    # for i in arr:
    #     if i < min_num:
    #         min_num = i
    # return min_num

def maximum(arr):
# 1st solution
    return max(arr)

# 2nd solution
    # return sorted(arr)[-1]

# 3rd solution
    # max_num = arr[0]
    # for i in arr:
    #     if i > max_num:
    #         max_num = i
    # return max_num




print(minimum([-52, 56, 30, 29, -54, 0, -110])) # -110
print(minimum([42, 54, 65, 87, 0])) # 0
print(minimum([1, 2, 3, 4, 5, 10])) # 1
print(minimum([-1, -2, -3, -4, -5, -10])) # -10
print(minimum([9])) # 9


print(maximum([-52, 56, 30, 29, -54, 0, -110])) # 56
print(maximum([4,6,2,1,9,63,-134,566])) # 566
print(maximum([5])) # 5
print(maximum([534,43,2,1,3,4,5,5,443,443,555,555])) # 555
print(maximum([9])) # 9