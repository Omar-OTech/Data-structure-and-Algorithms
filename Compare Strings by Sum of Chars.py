def compare(s1, s2):
    s1 = s1 or ""
    s2 = s2 or ""
    
    if not s1.isalpha():
        s1 = ""
    if not s2.isalpha():
        s2 = ""
    
    sum_s1 = sum(ord(char) for char in s1.upper())
    sum_s2 = sum(ord(char) for char in s2.upper())
    
    return sum_s1 == sum_s2




print(compare("AD", "BC"))           # True
print(compare("AD", "DD"))           # False
print(compare("gf", "FG"))           # True
print(compare("Ad", "DD"))           # False
print(compare("zz1", ""))            # True
print(compare("ZzZz", "ffPFF"))      # True
print(compare("kl", "lz"))           # False
print(compare(None, ""))             # True
print(compare("!!", "7476"))         # True
print(compare("##", "1176"))         # True