def simple_multiplication(number):
# 1st solution
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

# 2nd solution
    # return number * 8 if number % 2 == 0 else number * 9
    # return number * 9 if number % 2 else number * 8

# 3rd solution
    return number * (8 + number % 2)



print(simple_multiplication(2)) # 16
print(simple_multiplication(1)) # 9
print(simple_multiplication(8)) # 64
print(simple_multiplication(4)) # 32
print(simple_multiplication(5)) # 45