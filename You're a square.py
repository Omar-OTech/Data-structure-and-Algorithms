import math
def is_square(n):
# 1st solution
    if n < 0:
        return False
    else:
        return n**0.5 == int(n**0.5)

# 2nd solution
    # if n < 0:
    #     return False
    # else:
    #     return math.sqrt(n).is_integer()




print(is_square(-1))        # False, "-1: Negative numbers cannot be square numbers"
print(is_square( 0))        # True, "0 is a square number (0 * 0)"
print(is_square( 3))        # False, "3 is not a square number"
print(is_square( 4))        # True, "4 is a square number (2 * 2)"
print(is_square(25))        # True, "25 is a square number (5 * 5)"
print(is_square(26))        # False, "26 is not a square number"