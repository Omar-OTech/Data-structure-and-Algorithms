def correct(s):
# 1st solution
    return s.replace("5", "S").replace("0", "O").replace("1", "I")

# 2nd solution
    # res = ""
    # for i in s:
    #     if i == "5":
    #         res += "S"
    #     elif i == "0":
    #         res += "O"
    #     elif i == "1":
    #         res += "I"
    #     else:
    #         res += i
    # return res

# 3rd solution
    # val = str.maketrans("501", "SOI")
    # return s.translate(mapping)

print(("L0ND0N"))      # "LONDON"
print(("DUBL1N"))      # "DUBLIN"
print(("51NGAP0RE"))   # "SINGAPORE"
print(("BUDAPE5T"))    # "BUDAPEST"
print(("PAR15"))       # "PARIS"