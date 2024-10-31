def solve(s):
    # [uppercase, lowercase, number, specialCharacter]
    res = [0, 0, 0, 0]
    for char in s:
        if char.isupper():
            res[0] += 1
        elif char.islower():
            res[1] += 1
        elif char.isdigit():
            res[2] += 1
        else:
            res[3] += 1

    return res


# 2nd solution
#   uc, lc, num, sp = 0, 0, 0, 0
#   for ch in s:
#     if ch.isupper(): uc += 1
#     elif ch.islower(): lc += 1
#     elif ch.isdigit(): num += 1
#     else: sp += 1
#   return [uc, lc, num, sp]



print(solve("Codewars@codewars123.com"))                   # [1,18,3,2]
print(solve("bgA5<1d-tOwUZTS8yQ"))                         # [7,6,3,2]
print(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"))          # [9,9,6,9]
print(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"))     # [15,8,6,9]
print(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe"))                 # [10,7,3,6]
print(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"))         # [7,13,4,10]