def replace_exclamation(st):
    return ''.join('!' if i in 'aeiouAEIOU' else i for i in st)

print(replace_exclamation("Hi!"))           # "H!!"
print(replace_exclamation("!Hi! Hi!"))      # "!H!! H!!"
print(replace_exclamation("aeiou"))         # "!!!!!"
print(replace_exclamation("ABCDE"))         # "!BCD!"