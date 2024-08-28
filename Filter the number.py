def filter_string(st):
# 1st solution
    for i in st:
        if not i.isdigit():
            st = st.replace(i, "")
    return int(st)

# 2nd solution
    # return int("".join(i for i in st if i.isdigit()))
    # or
    # return int("".join(filter(str.isdigit, st)))


print(filter_string("123"))             # 123, 'Just return the numbers'
print(filter_string("a1b2c3"))          # 123, 'Just return the numbers'
print(filter_string("aa1bb2cc3dd"))     # 123, 'Just return the numbers'
print(filter_string("aa 112 3dd"))      # 1123, 'Just return the numbers'
print(filter_string("11bb2c23c3"))      # 112233, 'Just return the numbers'