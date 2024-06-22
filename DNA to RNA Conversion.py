def dna_to_rna(dna):
# 1st solution
    return dna.replace("T", "U")

# 2nd solution
    # RNA = ""
    # for i in dna:
    #     if i == "T":
    #         RNA += "U"
    #     else:
    #         RNA += i
    # return RNA

print(dna_to_rna("TTTT"))           # "UUUU"
print(dna_to_rna("GCAT"))           # "GCAU"
print(dna_to_rna("GACCGCCGCC"))     # "GACCGCCGCC"