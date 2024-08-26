def who_is_paying(name):
    res = []
    if len(name) <= 2:
        res.append(name)
    else:
        res.append(name)
        res.append(name[:2])
    return res

# 2nd solution
    # return [name, name[0:2]] if len(name) > 2 else [name]

print(who_is_paying("Mexico"))         # ["Mexico", "Me"]
print(who_is_paying("Melania"))        # ["Melania", "Me"]
print(who_is_paying("Melissa"))        # ["Melissa", "Me"]
print(who_is_paying("Me"))             # ["Me"]
print(who_is_paying(""))               # [""]
print(who_is_paying("I"))              # ["I"]