def multiply(n):
    num_digits = len(str(abs(n)))
    return n * (5 ** num_digits)


print(multiply(10))          # 250
print(multiply(5))           # 25
print(multiply(200))         # 25000
print(multiply(0))           # 0
print(multiply(-2))          # -10