def highest_rank(arr):
    sorted_arr = sorted(arr, reverse=True)
    return max(sorted_arr, key=sorted_arr.count)

print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))                   # 12
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))                   # 10
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]))               # 12
print(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]))       # 3
print(highest_rank([1, 2, 3]))                                          # 3
print(highest_rank([1, 1, 2, 3]))                                       # 1
print(highest_rank([1, 1, 2, 2, 3]))                                    # 2