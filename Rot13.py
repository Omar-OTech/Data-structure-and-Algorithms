def rot13(message):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rot13 = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    return message.translate(str.maketrans(letters, rot13))



print(rot13('test'))                  # 'grfg', 'Returned solution incorrect for fixed string = test'
print(rot13('Test'))                  # 'Grfg', 'Returned solution incorrect for fixed string = Test'
print(rot13('aA bB zZ 1234 *!?%'))    # 'nN oO mM 1234 *!?%', 'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%'