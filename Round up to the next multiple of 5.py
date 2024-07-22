def round_to_next5(n):
# 1st solution
    if n % 5 == 0:
        return n
    else:
        return n + 5 - n % 5

# 2nd solution
    # while n % 5 != 0:
    #     n += 1
    # return n

print(round_to_next5(0))    # 0
print(round_to_next5(1))    # 5
print(round_to_next5(3))    # 5
print(round_to_next5(5))    # 5
print(round_to_next5(7))    # 10
print(round_to_next5(39))   # 40
print(round_to_next5(42))   # 45
print(round_to_next5(45))   # 45
print(round_to_next5(47))   # 50