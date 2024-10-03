def find_digit(num, nth):   
    if nth <= 0:
        return -1
    num = abs(num)
    num_str = str(num)
    if nth > len(num_str):
        return 0
    return int(num_str[-nth])

print(find_digit(5673, 4))         # 5
print(find_digit(129, 2))          # 2
print(find_digit(-2825, 3))        # 8
print(find_digit(0, 20))           # 0
print(find_digit(65, 0))           # -1
print(find_digit(24, -8))          # -1
print(find_digit(-456, 5))         # 0
print(find_digit(-1234, 2))        # 3
print(find_digit(-5540, 1))        # 0
print(find_digit(678998, 0))       # -1
print(find_digit(-67854, -57))     # -1
print(find_digit(0, -3))           # -1 