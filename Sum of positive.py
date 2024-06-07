def positive_sum(arr):
# 1at solution
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum

# 2nd solution
    # return sum(i for i in arr if i > 0)


print(positive_sum([1,2,3,4,5]))            # 15
print(positive_sum([1,-2,3,4,5]))           # 13
print(positive_sum([-1,2,3,4,-5]))          # 9
print(positive_sum([]))                     # 0
print(positive_sum([-1,-2,-3,-4,-5]))       # 0