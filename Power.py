def number_to_pwr(number, p):
    result = 1
    for _ in range(p):
        result *= number
    return result


print(number_to_pwr(4, 2))    # 16
print(number_to_pwr(10, 3))   # 1000
print(number_to_pwr(2, 8))    # 256
print(number_to_pwr(10, 0))    # 1
print(number_to_pwr(8, 2))    # 64