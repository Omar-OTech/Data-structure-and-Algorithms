def convert_bits(a, b):
    return bin(a ^ b).count('1')



print(convert_bits(31, 14))     # 2
print(convert_bits(7, 17))      # 3
print(convert_bits(31, 0))      # 5
print(convert_bits(0, 0))       # 0