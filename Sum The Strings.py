def sum_str(a, b):
# 1st solution
    if type(a) == str  and type(b) == str:
        if a == "" and b == "":
            return "0"
        elif a == "":
            return b
        elif b == "":
            return a
        else:
            return str(int(a) + int(b))


# 2nd solution
    # return str(int(a or 0) + int(b or 0))

print(sum_str("4","5"))   # "9"
print(sum_str("34","5"))  # "39"
print(sum_str("9",""))    # "9", "x + empty = x"
print(sum_str("","9"))    # "9", "empty + x = x"
print(sum_str("",""))     # "0", "empty + empty = 0"