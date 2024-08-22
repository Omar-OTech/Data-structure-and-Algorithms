def factorial(n):
    if n > 12 or n < 0:
        raise ValueError
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(0))       # 1, "factorial for 0 is 1
print(factorial(1))       # 1, "factorial for 1 is 1
print(factorial(2))       # 2, "factorial for 2 is 2
print(factorial(3))       # 6, "factorial for 3 is 6
    