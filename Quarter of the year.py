def quarter_of(month):
# 1st solution
    return (month + 2) // 3


# 2nd solution
    # if month in range(1, 4):
    #     return 1
    # elif month in range(4, 7):
    #     return 2
    # elif month in range(7, 10):
    #     return 3
    # else:
    #     return 4


print(quarter_of(3))        # 1
print(quarter_of(8))        # 3
print(quarter_of(11))       # 4
print(quarter_of(12))       # 4
print(quarter_of(1))        # 1
print(quarter_of(4))        # 2
print(quarter_of(6))        # 2