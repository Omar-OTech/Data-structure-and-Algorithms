def summation(num):
# 1st solution
    # res = 0
    # for i in range(1, num + 1):
    #     res += i
    # return res

# 2nd solution
    return sum(range(1,num+1))

print(summation(1))      # 1
print(summation(8))      # 36
print(summation(22))     # 253
print(summation(100))    # 5050
print(summation(213))    # 22791