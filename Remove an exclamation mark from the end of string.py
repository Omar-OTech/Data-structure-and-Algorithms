def remove(s):
# 1st solution
    res = ""
    for i in s:
        if i[-1] == "!":
            res = s[:-1]
        else:
            res = s
    return res

# 2nd solution
    # return s[:-1] if s.endswith("!") else s

# 3rd solution
    # return s.rstrip("!")

# 4th solution
    # return s[:-1] if s and s[-1] == "!" else s

# 5th solution
    # return s.removesuffix("!")

print(remove("Hi!"))    # "Hi"
print(remove("Hi!!!"))    # "Hi!!"
print(remove("!Hi"))    # "!Hi"
print(remove("!Hi!"))    # "!Hi"
print(remove("Hi! Hi!"))    # "Hi! Hi"
print(remove("Hi"))    # "Hi"
print(remove("Hi! Hi!!"))    # "Hi! Hi!"
print(remove("Hi! Hi!!!"))    # "Hi! Hi!!"
