def is_vow(inp):
    res = []
    for i in inp:
        if i == 97:
            res.append('a')
        elif i == 101:
            res.append('e')
        elif i == 105:
            res.append('i')
        elif i == 111:
            res.append('o')
        elif i == 117:
            res.append('u')
        else:
            res.append(i)
    return res

# 2nd solution
# return [chr(i) if chr(i) in "aeiou" else i for i in inp]

print(is_vow([118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ]))        # [118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106 ]
print(is_vow(["e",121,110,113,113,103,121,121,"e",107,103 ]))                                # [101,121,110,113,113,103,121,121,101,107,103 ]
print(is_vow([118,103,110,109,104,106 ]))                                                    # [118,103,110,109,104,106 ]
print(is_vow([107,99,110,107,118,106,112,102 ]))                                             # [107,99,110,107,118,106,112,102 ]
print(is_vow([100,100,116,"i","u",121 ]))                                                    # [100,100,116,105,117,121 ]