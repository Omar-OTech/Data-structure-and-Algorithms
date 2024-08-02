def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    else:
        return sum([i for i in range(n, m, n)])

print(sum_mul(0, 0))         # 'INVALID
print(sum_mul(2, 9))         # 20
print(sum_mul(4, -7))        # 'INVALID
print(sum_mul(4, 123))       # 1860
print(sum_mul(123, 4567))    # 86469
print(sum_mul(2, 10))        # 20
print(sum_mul(2, 2))         # 0
print(sum_mul(7, 7))         # 0
print(sum_mul(7, 2))         # 0
print(sum_mul(21, 3))        # 0
print(sum_mul(0, 2))         # 'INVALID
print(sum_mul(2, 0))         # 'INVALID
print(sum_mul(4, -7))        # 'INVALID
print(sum_mul(-7, 4))        # 'INVALID       