def between(a, b):
# 1st solution
    if a < b:
        return list(range(a, b+1))

# 2nd solution
    # if a < b:
    #     for i in range(a, b + 1):
    #         return i


print(between(1, 4))     #   [1, 2, 3, 4]
print(between(-2, 2))    #   [-2, -1, 0, 1, 2]
