def enough(cap, on, wait):
# 1st solution
    fit = cap - on
    if fit >= wait:
        return 0
    else:
        return wait - fit

# 2nd solution
    # return max(0, wait - (cap - on))

print(enough(10, 5, 5))    # 0
print(enough(100, 60, 50)) # 10
print(enough(20, 5, 5))    # 0