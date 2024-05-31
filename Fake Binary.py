def fake_bin(x):
# 1st solution
    res = ''
    for i in x:
        if int(i) >= 5:
            res += '1'
        else:
            res += '0'
    return res

# 2nd solution
    # return ''.join('0' if i < '5' else '1' for i in x)

# 3rd solution
    # return ''.join('0' if int(i) < 5  else '1' for i in x)

# 4th solution
    # return ''.join([str(int(i) // 5) for i in x])







print(fake_bin('45385593107843568')) # '01011110001100111'
print(fake_bin('509321967506747')) # '101000111101101'
print(fake_bin('366058562030849490134388085')) # '011011110000101010000011011'
print(fake_bin('15889923')) # '01111100'
print(fake_bin('800857237867')) # '100111001111'