def DNA_strand(dna):
# 1st solution
    res = ""
    for i in dna:
        if i == "A":
            res += "T"
        elif i == "T":
            res += "A"
        elif i == "C":
            res += "G"
        elif i == "G":
            res += "C"
    return res

# 2nd solution
    # return dna.translate(str.maketrans("ATCG", "TAGC"))

# 3rd solution
    # dict ={"A": "T", "T": "A", "C": "G", "G": "C"}
    # return "".join(dict[i] for i in dna)
print(DNA_strand("AAAA"))     #  "TTTT","String AAAA is"
print(DNA_strand("ATTGC"))    #  "TAACG","String ATTGC is"
print(DNA_strand("GTAT"))     #  "CATA","String GTAT is"