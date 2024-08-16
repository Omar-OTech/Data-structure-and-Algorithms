def remove(st):
# 1st solution
    while st and st[-1] == "!":
        st = st[:-1]
    return st

# 2nd solution
    # return st.rstrip("!")



print(remove("Hi!"))                   # "Hi"
print(remove("Hi!!!"))                 # "Hi"
print(remove("!Hi"))                   # "!Hi"
print(remove("!Hi!"))                  # "!Hi"
print(remove("Hi! Hi!"))               # "Hi! Hi"
print(remove("Hi"))                    # "Hi"
print(remove(""))                      # ""
print(remove("!!!"))                   # ""
print(remove("Hi! Hi! Hi!"))           # "Hi! Hi! Hi"
print(remove("Hi! Hi! Hi"))            # "Hi! Hi! Hi"