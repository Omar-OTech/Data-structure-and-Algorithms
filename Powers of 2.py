def powers_of_two(n):
    res = []
    for i in range(n + 1):
        res.append(2 ** i)
    return res

print(powers_of_two(0))     # [1]
print(powers_of_two(1))     # [1, 2]
print(powers_of_two(4))     # [1, 2, 4, 8, 16]