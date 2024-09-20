def max_diff(lst):
    sorted_arr = sorted(lst)
    return sorted_arr[-1] - sorted_arr[0] if sorted_arr else 0

# 2nd solution
    # return max(lst) - min(lst) if lst else 0

print(max_diff([0, 1, 2, 3, 4, 5, 6]))        # 6
print(max_diff([-0, 1, 2, -3, 4, 5, -6]))     # 11
print(max_diff([0, 1, 2, 3, 4, 5, 16]))       # 16
print(max_diff([16]))                         # 0
print(max_diff([]))                           # 0