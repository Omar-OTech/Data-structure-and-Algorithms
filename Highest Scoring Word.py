def high(x):
    split = x.split()
    score = 0
    word = ''
    for i in split:
        temp = 0
        for j in i:
            temp += ord(j) - 96
        if temp > score:
            score = temp
            word = i
    return word

print(high('man i need a taxi up to ubud'))                        # 'taxi'
print(high('what time are we climbing up the volcano'))            # 'volcano'
print(high('take me to semynak'))                                  # 'semynak'
print(high('aa b'))                                                # 'aa'
print(high('b aa'))                                                # 'b'
print(high('bb d'))                                                # 'bb'
print(high('d bb'))                                                # 'd'
print(high("aaa b"))                                               # "aaa"