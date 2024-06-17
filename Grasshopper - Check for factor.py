def check_for_factor(base, factor):
# 1st solution
    if base % factor == 0:
        return True
    else:
        return False

# 2nd solution
    # return base % factor == 0

print(check_for_factor(10, 2))           # True
print(check_for_factor(63, 7))           # True
print(check_for_factor(2450, 5))         # True
print(check_for_factor(24612, 3))        # True
print(check_for_factor(9, 2))            # False
print(check_for_factor(653, 7))          # False
print(check_for_factor(2453, 5))         # False
print(check_for_factor(24617, 3))        # False