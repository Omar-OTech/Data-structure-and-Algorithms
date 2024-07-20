def solve(s):
# 1st solution
    res = 0
    for i in s:
        if i.isupper():
            res += 1
    return s.upper() if res > len(s) / 2 else s.lower()


# 2nd solution
    # uppwer = 0
    # lower = 0
    # for i in s:
    #     if i.isupper():
    #         uppwer += 1
    #     else:
    #         lower += 1
    # return s.upper() if uppwer > lower else s.lower()

print(solve("code"))   # "code"
print(solve("CODe"))   # "CODE"
print(solve("COde"))   # "code"
print(solve("Code"))   # "code"