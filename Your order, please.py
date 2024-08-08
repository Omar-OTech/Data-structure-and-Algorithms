def order(sentence):
    res = ''
    for i in range(1, 10):
        for word in sentence.split():
            if str(i) in word:
                res += word + ' '
    return res.strip()


# 2nd solution
# def order(sentence):
#     return ' '.join(sorted(sentence.split(), key=lambda x: sorted(x)))


print(order("is2 Thi1s T4est 3a"))                   # "Thi1s is2 3a T4est"
print(order("4of Fo1r pe6ople g3ood th5e the2"))     # "Fo1r the2 g3ood 4of th5e pe6ople"
print(order(""))                                     # ""