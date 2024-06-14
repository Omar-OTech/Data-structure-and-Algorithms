def find_smallest_int(arr):
# 1st solution
    return min(arr)

# 2nd solution
    # sorted_arr = sorted(arr)
    # return sorted_arr[0]

# 3rd solution
    # smallest_number = arr[0]
    # for i in range(1, len(arr)):
    #     if arr[i] < smallest_number:
    #         smallest_number = arr[i]
    # return smallest_number

print(find_smallest_int([78, 56, 232, 12, 11, 43]))        # 11
print(find_smallest_int([78, 56, -2, 12, 8, -33]))         # -33
print(find_smallest_int([0, 1-2**64, 2**64]))              # 1-2**64