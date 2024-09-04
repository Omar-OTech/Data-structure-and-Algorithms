def power_of_two(x):
    if x == 0:
        return False
    while x != 1:
        if x % 2 != 0:
            return False
        x = x // 2
    return True


print(power_of_two(0))         # False
print(power_of_two(1))         # True
print(power_of_two(2))         # True
print(power_of_two(5))         # False
print(power_of_two(6))         # False
print(power_of_two(4096))      # True