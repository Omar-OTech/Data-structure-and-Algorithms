def add_length(str_):
# 1st solution
    str_ = str_.split()
    return [f'{i} {len(i)}' for i in str_]

# 2nd solution
    # res = []
    # str_ = str_.split()
    # for i in str_:
    #     res.append(f'{i} {len(i)}')
    # return res

print(add_length('apple ban'))     # ["apple 5", "ban 3"])
print(add_length('you will win'))  # ["you 3", "will 4", "win 3"])
print(add_length('you'))           # ["you 3"])
print(add_length('y'))             # ["y 1"])