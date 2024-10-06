def is_digit(s):
    if not s or s.isspace():
        return False
    
    s = s.strip()
    
    if s[0] == '-':
        s = s[1:]
    
    if not s:
        return False
    
    decimal_count = 0
    for i, char in enumerate(s):
        if char == '.':
            decimal_count += 1
            if decimal_count > 1 or i == 0 or i == len(s) - 1:
                return False
        elif not char.isdigit():
            return False
    
    return True


print(is_digit("s2324"))    # False
print(is_digit("-234.4"))   # True
print(is_digit("3 4"))      # False
print(is_digit("3-4"))      # False
print(is_digit("3 4   "))   # False
print(is_digit("34.65"))    # True
print(is_digit("-0"))       # True
print(is_digit("0.0"))      # True
print(is_digit(""))         # False
print(is_digit(" "))        # False