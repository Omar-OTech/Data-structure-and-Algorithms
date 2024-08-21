def vowel_indices(word):
    return [i for i, c in enumerate(word, 1) if c.lower() in "aeiouy"]

print(vowel_indices("mmm"))            # [], "failed on the word 'mmm'")
print(vowel_indices("apple"))          # [1,5], "failed on the word 'apple'")
print(vowel_indices("123456"))         # [], "failed on the word '123456'")
print(vowel_indices("UNDISARMED"))     # [1,4,6,9], "failed on the word 'UNDISARMED'. Consider case")