def sum_mix(arr):
# 1st solution
    for i in range(len(arr)):
        if type(arr[i]) == str:
            arr[i] = int(arr[i])
    return sum(arr)

# 2nd solution
    # return sum(map(int, arr))

# 3rd solution
    # res = []
    # for i in arr:
    #     res.append(int(i))
    # return sum(res)


print(sum_mix([9, 3, '7', '3']))                         # 22
print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))        # 42
print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']))    # 41
print(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']))         # 45
print(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]))     # 61