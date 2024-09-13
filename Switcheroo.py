def switcheroo(s):
    return s.translate(str.maketrans('ab', 'ba'))


# 2nd solution
# def switcheroo(s):
#     return ''.join(['b' if i == 'a' and i in s else 'a' if i == 'b' and i in s else i for i in s])

print(switcheroo("abc"))                  # "bac"
print(switcheroo('aaabcccbaaa'))          # 'bbbacccabbb'
print(switcheroo('ccccc'))                # 'ccccc'
print(switcheroo('abababababababab'))     # 'babababababababa'
print(switcheroo('aaaaa'))                # 'bbbbb'