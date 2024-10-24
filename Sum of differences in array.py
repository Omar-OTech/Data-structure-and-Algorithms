def sum_of_differences(arr):
    if not arr or len(arr) == 1:
        return 0
    arr = sorted(arr, reverse=True)
    result = 0
    for i in range(len(arr) - 1):
        result += arr[i] - arr[i + 1]
    return result

# 2nd solution
    # return max(arr) - min(arr) if arr else 0


print(sum_of_differences([1, 2, 10]))           #  9
print(sum_of_differences([-3, -2, -1]))         #  2
print(sum_of_differences([1, 1, 1, 1, 1]))      #  0
print(sum_of_differences([-17, 17]))            #  34)     
print(sum_of_differences([]))                   #  0
print(sum_of_differences([0]))                  #  0
print(sum_of_differences([-1]))                 #  0
print(sum_of_differences([1]))                  #  0