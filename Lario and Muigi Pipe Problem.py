def pipe_fix(nums):
# 1st solution
    res = []
    start = nums[0]
    end = nums[-1]
    for i in range(start, end + 1):
        res.append(i)
    return res

# 2nd solution
    # return list(range(min(nums), max(nums) + 1))

# 3rd solution
    # return list(range(nums[0], nums[-1] + 1))

print(pipe_fix([1, 2, 3, 5, 6, 8, 9]))    #  [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(pipe_fix([1, 2, 3, 12]))            #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(pipe_fix([6, 9]))                   #  [6, 7, 8, 9])
print(pipe_fix([-1, 4]))                  #  [-1, 0, 1, 2, 3, 4])
print(pipe_fix([1, 2, 3]))                #  [1, 2, 3])