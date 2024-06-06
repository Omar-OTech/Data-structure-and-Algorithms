def get_middle(s):
    start = len(s) // 2 - 1
    print(start)
    end = len(s) // 2 + 1
    print(end)
    # if len(s) % 2 == 0:
    #     return s[start:end]
    # if len(s) % 2 != 0:
    #     return s[len(s) // 2]



print(get_middle("test"))     # "es"
print(get_middle("testing"))  # "t"
print(get_middle("middle"))   # "dd"
print(get_middle("A"))        # "A"
print(get_middle("of"))       # "of"