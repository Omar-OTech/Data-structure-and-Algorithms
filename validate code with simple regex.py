def validate_code(code):
# 1st solution
    return str(code).startswith(('1', '2', '3'))

# 2nd solution
    # return str(code)[0] in '123'

# 3rd solution
    # string = str(code)
    # return string[0] in '123'



print(validate_code(123))      # True
print(validate_code(248))      # True
print(validate_code(8))        # False
print(validate_code(321))      # True
print(validate_code(9453))     # False