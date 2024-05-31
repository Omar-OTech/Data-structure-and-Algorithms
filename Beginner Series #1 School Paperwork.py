def paperwork(n, m):
# 1st solution
    if n < 0 or m < 0:
        return 0
    return n * m

# 2nd solution
    # return 0 if n < 0 or m < 0 else n * m

# 3rd solution
    # return max(0, n) * max(0, m)










print(paperwork(5,5)) # 25, "Failed at Paperwork(5,5)"
print(paperwork(1,2)) # 2, "Failed at Paperwork(1,2)"
print(paperwork(-5,5)) # 0, "Failed at Paperwork(-5,5)"
print(paperwork(5,-5)) # 0, "Failed at Paperwork(5,-5)"
print(paperwork(-5,-5)) # 0, "Failed at Paperwork(-5,-5)"
