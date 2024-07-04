def shortcut( s ):
    vowels = ["a", "e", "i", "o", "u"]
    res = ''
    for i in s:
        if i not in vowels:
            res += i
    return res

print(shortcut("hello"))                #  "hll"
print(shortcut("hellooooo"))            #  "hll"
print(shortcut("how are you today?"))   #  "hw r y tdy?"
print(shortcut("complain"))             #  "cmpln"
print(shortcut("never"))                #  "nvr"