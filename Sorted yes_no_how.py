def is_sorted_and_how(arr):
# 1st solution
    if arr == sorted(arr):
        return 'yes, ascending'
    elif arr == sorted(arr)[::-1]:
        return 'yes, desending'
    else:
        return 'no'


# 2nd solution
    # is_ascending = True
    # is_desending = True
    # for i in range(len(arr) - 1):
    #     if arr[i] > arr[i + 1]:
    #         is_ascending = False
    #     if arr[i] < arr[i + 1]:
    #         is_desending = False
    # if is_ascending:
    #     return 'yes, ascending'
    # elif is_desending:
    #     return 'yes, desending'
    # else:
    #     return 'no'
    
print(is_sorted_and_how([1, 2]))             # 'yes, ascending'
print(is_sorted_and_how([15, 7, 3, -8]))     # 'yes, descending'
print(is_sorted_and_how([4, 2, 30]))         # 'no'