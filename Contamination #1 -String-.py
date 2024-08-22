def contamination(text, char):
# 1st solution
    if text == "" or char == "":
        return ""
    elif text == char:
        return char
    else:
        return char * len(text)
    
# 2nd solution
    # return char * len(text) if text else ""

print(contamination("abc","z"))            # "zzz"
print(contamination("","z"))               # ""
print(contamination("abc",""))             # ""
print(contamination("_3ebzgh4","&"))       # "&&&&&&&&"
print(contamination("//case"," "))         # "      "
