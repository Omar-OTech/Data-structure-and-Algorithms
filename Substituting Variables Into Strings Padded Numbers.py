def solution(value):
    res = str(value)
    return 'Value is ' + '0' * (5-len(res)) + res

# 2nd solution
    # return 'Value is {:05}'.format(value)

# 3rd solution
    # return 'Value is ' + str(value).zfill(5)
    
# 4th solution
    # return 'Value is %05d' % value
    
print(solution(0))       # 'Value is 00000'
print(solution(5))       # 'Value is 00005'
print(solution(109))     # 'Value is 00109'
print(solution(1204))    # 'Value is 01204'