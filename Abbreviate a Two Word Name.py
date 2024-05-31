def abbrev_name(name):
# 1st solution
    return '.'.join([i[0].upper() for i in name.split(' ')])

# 2nd solution
    # res = []
    # split = name.split(' ')
    # for i in split:
    #     res.append(i[0].upper())
    # return '.'.join(res)




print(abbrev_name("Sam Harris"))     # "S.H"
print(abbrev_name("patrick feenan")) # "P.F"
print(abbrev_name("Evan C"))         # "E.C"
print(abbrev_name("P Favuzzi"))      # "P.F"
print(abbrev_name("David Mendieta")) # "D.M"