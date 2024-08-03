def capitalize(s):
    res = []
    odd = ""
    even = ""
    for i in range(len(s)):
        if i % 2 == 0:
            odd += s[i].upper()
            even += s[i]
        else:
            odd += s[i]
            even += s[i].upper()
    res.append(odd)
    res.append(even)
    return res

print(capitalize("abcdef"))                   # ['AbCdEf', 'aBcDeF'])
print(capitalize("codewars"))                 # ['CoDeWaRs', 'cOdEwArS'])
print(capitalize("abracadabra"))              # ['AbRaCaDaBrA', 'aBrAcAdAbRa'])
print(capitalize("codewarriors"))             # ['CoDeWaRrIoRs', 'cOdEwArRiOrS'])
print(capitalize("indexinglessons"))          # ['InDeXiNgLeSsOnS', 'iNdExInGlEsSoNs'])
print(capitalize("codingisafunactivity"))     # ['CoDiNgIsAfUnAcTiViTy', 'cOdInGiSaFuNaCtIvItY'])