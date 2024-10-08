def capitalize(s, ind):
    # res = ''
    # for i in range(len(s)):
    #     if i in ind:
    #         res += s[i].upper()
    #     else:
    #         res += s[i]
    # return res


# 2nd solution
    return ''.join([c.upper() if i in ind else c for i, c in enumerate(s)])


print(capitalize("abcdef",[1,2,5]))             #'aBCdeF'
print(capitalize("abcdef",[1,2,5,100]))         #'aBCdeF',
print(capitalize("codewars",[1,3,5,50]))        #'cOdEwArs'
print(capitalize("abracadabra",[2,6,9,10]))     #'abRacaDabRA'
print(capitalize("codewarriors",[5]))           #'codewArriors'