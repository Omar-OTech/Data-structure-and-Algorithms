def swap(st):
    vowel = "aeiouAEIOU"
    res = ""
    for char in st:
        if char in vowel:
            res += char.upper()
        else:
            res += char
    return res


print(swap("HelloWorld!"))     # "HEllOWOrld!"
print(swap("Sunday"))          # "SUndAy"
print(swap("Codewars"))        # "COdEwArs"
print(swap("Monday"))          # "MOndAy"
print(swap("Friday"))          # "FrIdAy"
print(swap("abracadabra"))     # "AbrAcAdAbrA"