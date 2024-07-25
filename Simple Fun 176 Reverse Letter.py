def reverse_letter(st):
    res = ''
    for i in st:
        if i.isalpha():
            res += i
    return res[::-1]


print(reverse_letter("krishan"))      #"nahsirk"
print(reverse_letter("ultr53o?n"))    #"nortlu"
print(reverse_letter("ab23c"))        #"cba"
print(reverse_letter("krish21an"))    #"nahsirk"