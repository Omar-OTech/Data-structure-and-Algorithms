def accum(st):
# 1st solution
    res = []
    for i in range(len(st)):
        res.append(st[i].upper() + st[i].lower() * i)
    return '-'.join(res)



# 2nd solution
    # result = []
    # for i, char in enumerate(st):
    #     result.append(char.upper() + char.lower() * i)
    # return '-'.join(result)


print(accum("ZpglnRxqenU")) # "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
print(accum("NyffsGeyylB")) # "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
print(accum("MjtkuBovqrU")) # "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
print(accum("EvidjUnokmM")) # "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"
print(accum("HbideVbxncC")) # "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"