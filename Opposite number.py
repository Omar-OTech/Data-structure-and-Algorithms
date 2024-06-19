def opposite(number):
# 1st solution
    if number < 0:
        return abs(number)
    else:
        return -number

# 2nd solution
    # return number * -1

print(opposite(1))               # -1
print(opposite(25.6))            # -25.6
print(opposite(0))               # 0
print(opposite(1425.2222))       # -1425.2222
print(opposite(-3.1458))         # 3.1458
print(opposite(-95858588225))    # 95858588225