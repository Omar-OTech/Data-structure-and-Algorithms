def logical_calc(array, op):
    if op == "AND":
        return all(array)
    elif op == "OR":
        return any(array)
    elif op == "XOR":
        return sum(array) % 2 == 1
    else:
        return None

# 2nd solution
    # res = array[0]
    # for i in array[1:]:
    #     if op == "AND":
    #         res &= i
    #     elif op == "OR":
    #         res |= i
    #     elif op == "XOR":
    #         res ^= i
    # return res


print(logical_calc([True, False], "AND"))           # False
print(logical_calc([True, False], "OR"))            # True
print(logical_calc([True, False], "XOR"))           # True
print(logical_calc([True, True, False], "AND"))     # False
print(logical_calc([True, True, False], "OR"))      # True
print(logical_calc([True, True, False], "XOR"))     # False