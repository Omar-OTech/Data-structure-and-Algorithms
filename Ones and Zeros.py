def Ones_and_Zeros(x):
# 1st solution
    # val = [8, 4, 2, 1]
    # count = 0
    # for i in range(len(x)):
    #     count += x[i] * val[i]
    # return count

# 2nd solution
    res = 0
    x.reverse()
    for i in range(len(x)):
        res += x[i] * 2 ** i
    return res


print(Ones_and_Zeros([0, 0, 0, 1]))
print(Ones_and_Zeros([0, 0, 1, 0]))
print(Ones_and_Zeros([0, 1, 0, 0]))
print(Ones_and_Zeros([1, 0, 0, 0]))
print(Ones_and_Zeros([0, 0, 1, 1]))
print(Ones_and_Zeros([1, 1, 1, 1]))
print(Ones_and_Zeros([0, 1, 1, 0]))