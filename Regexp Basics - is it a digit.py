def is_digit(n):
    return True if n.isdigit() and len(n) == 1 else False


print((is_digit("")))  # False
print((is_digit("7")))  # True
print((is_digit(" ")) ) # False
print((is_digit("a")))  # False
print((is_digit("a5")))  # False