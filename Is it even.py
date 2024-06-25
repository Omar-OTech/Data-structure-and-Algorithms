def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(0))           # True
print(is_even(0.5))         # False
print(is_even(1))           # False
print(is_even(2))           # True
print(is_even(-4))          # True
print(is_even(15))          # False
print(is_even(20))          # True
print(is_even(220))         # True
print(is_even(222222221))   # False
print(is_even(500000000))   # True