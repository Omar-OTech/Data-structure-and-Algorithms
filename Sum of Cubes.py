def sum_cubes(n):
    res = 0
    for i in range(1, n+1):
        res += i**3
    return res

print(sum_cubes(1))         # 1
print(sum_cubes(2))         # 9
print(sum_cubes(3))         # 36
print(sum_cubes(4))         # 100
print(sum_cubes(10))        # 3025
print(sum_cubes(123))       # 58155876