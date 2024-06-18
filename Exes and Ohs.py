def xo(s):
# 1st solution
    s = s.lower()
    return s.count('x') == s.count('o')

# 2nd solution
    # xs = 0
    # os = 0
    # for i in s:
    #     if i.lower() == 'x':
    #         xs += 1
    #     elif i.lower() == 'o':
    #         os += 1
    # return xs == os


# Test cases
print(xo("ooxx")) # Expected: True
print(xo("xooxx")) # Expected: False
print(xo("ooxXm")) # Expected: True
print(xo("zpzpzpp")) # Expected: True
print(xo("zzoo")) # Expected: False
print(xo("zzoo")) # Expected: False
