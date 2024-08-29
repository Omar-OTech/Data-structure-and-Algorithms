def descending_order(num):
# 1st solution
    return int(''.join(sorted(str(num), reverse=True)))

# 2nd solution
    res = ''
    sorted_num = sorted(str(num), reverse=True)
    for i in sorted_num:
        res += i
    return int(res)

print(descending_order(0))    # 0
print(descending_order(1))    # 1
print(descending_order(15))   # 51
print(descending_order(123456789))   # 987654321