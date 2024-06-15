def sum_array(arr):
# 1st solution
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

# 2nd solution

    # if arr is None or len(arr) <= 2:
    #     return 0
    
    # min_val = min(arr)
    # max_val = max(arr)

    # min_count = arr.count(min_val)
    # max_count = arr.count(max_val)

    # res = [i for i in arr if i != min_val and i != max_val]

    # if min_count > 1:
    #     res.append(min_val * (min_count - 1))
    # if max_count > 1:
    #     res.append(max_val * (max_count - 1))

    # return sum(res)

print(sum_array(None))                          # 0
print(sum_array([]))                            # 0
print(sum_array([3]))                           # 0
print(sum_array([-3]))                          # 0
print(sum_array([ 3, 5]))                       # 0
print(sum_array([-3, -5]))                      # 0
print(sum_array([6, 2, 1, 8, 10]))              # 16
print(sum_array([6, 0, 1, 10, 10]))             # 17
print(sum_array([-6, -20, -1, -10, -12]))       # -28   
print(sum_array([-6, 20, -1, 10, -12]))         # 3     10 + (-1) + (-6) = 3