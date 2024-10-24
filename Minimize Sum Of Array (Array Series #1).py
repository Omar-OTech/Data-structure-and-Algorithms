def min_sum(arr):
    sort_arr = sorted(arr)
    sum = 0
    for i in range(len(sort_arr)// 2):
        sum += sort_arr[i] * sort_arr[-i-1]
    return sum

# 2nd solution
    # return sum(a * b for a, b in zip(sorted(arr), sorted(arr, reverse=True)))

# 3rd solution
    # sum(arr[i]*arr[-i-1] for i in range(len(arr)//2))


print(min_sum([5,4,2,3]))            # 22
print(min_sum([12,6,10,26,3,24]))    # 342
print(min_sum([9,2,8,7,5,4,0,6]))    # 74