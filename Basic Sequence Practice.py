def sum_of_n(n):
    res = [0]
    total = 0
    
    if n > 0:
        for i in range(1, n + 1):
            total += i
            res.append(total)
    elif n < 0:
        for i in range(-1, n - 1, -1):  # Start from -1 and go down to n
            total += i
            res.append(total)
            
    return res

print(sum_of_n(3))      # [0, 1, 3, 6]
print(sum_of_n(-4))     # [0, -1, -3, -6, -10]
print(sum_of_n(1))      # [0, 1]
print(sum_of_n(0))      # [0]
print(sum_of_n(10))     # [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
