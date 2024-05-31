def reverse_seq(n):
# 1st solution
    res = []
    for i in range(n, 0, -1):
        res.append(i)
    return res

# 2nd solution
    # res = []
    # for i in range(n):
    #     res.append(n - i)
    # return res

# 3rd solution
    # return list(range(n, 0, -1))

# 4th solution
    # res = []
    # for i in range(n):
    #     res.append(n)
    #     n -= 1
    # return res





print(reverse_seq(5)) # [5, 4, 3, 2, 1]
print(reverse_seq(6)) # [6, 5, 4, 3, 2, 1]
print(reverse_seq(7)) # [7, 6, 5, 4, 3, 2, 1]