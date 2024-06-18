def is_pangram(st):
# 1st solution
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    character = set(st.lower())
    return alphabet.issubset(character)

# 2nd solution
    st = st.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in st:
            return False
    return True










pangrams = [ 
    "The quick brown fox jumps over the lazy dog.",
    "Cwm fjord bank glyphs vext quiz",
    "Pack my box with five dozen liquor jugs.",
    "How quickly daft jumping zebras vex.",
    "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"
]

non_pangrams = [ 
    "This isn't a pangram!",
    "abcdefghijklm opqrstuvwxyz",
    "Aacdefghijklmnopqrstuvwxyz"
]

for p in pangrams:
    print(f'"{p}" is a pangram: {is_pangram(p)}')

for np in non_pangrams:
    print(f'"{np}" is a pangram: {is_pangram(np)}')