def solve(s):
    vowels = "aeiou"
    count = 0
    max_count = 0
    for i in s:
        if i in vowels:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    return max(max_count, count)

print((solve("")))                          # 0
print((solve("codewarriors")))              # 2
print((solve("suoidea")))                   # 3
print((solve("ultrarevolutionariees")))     # 3
print((solve("strengthlessnesses")))        # 1
print((solve("cuboideonavicuare")))         # 2
print((solve("chrononhotonthuooaos")))      # 5
print((solve("iiihoovaeaaaoougjyaw")))      # 8