def reverse_words(text):
# 1st solution
    # words = text.split(' ')
    # res = [word[::-1] for word in words]
    # return ' '.join(res)

# 2nd solution
    res = []
    word = text.split(' ')
    for i in word:
        res.append(i[::-1])
    return ' '.join(res)






print(reverse_words('The quick brown fox jumps over the lazy dog.')) # 'ehT kciuq nworb xof spmuj revo eht yzal .god'
print(reverse_words('apple'))                                        # 'elppa'
print(reverse_words('a b c d'))                                      # 'a b c d'
print(reverse_words('double  spaced  words'))                        # 'elbuod  decaps  sdrow'