def past(h, m, s):
# 1st solution
    return (h * 3600000) + (m * 60000) + (s * 1000)

# 2nd solution
    # ms = 0
    # ms += h * 3600000
    # ms += m * 60000
    # ms += s * 1000
    # return ms

print(past(0,1,1))  # 61000
print(past(1,1,1))  # 3661000
print(past(0,0,0))  # 0
print(past(1,0,1))  # 3601000
print(past(1,0,0))  # 3600000