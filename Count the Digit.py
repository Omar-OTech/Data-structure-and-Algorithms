def nb_dig(n, d):
    return sum(str(i * i).count(str(d)) for i in range(n + 1))


print(nb_dig(5750, 0))     #  4700
print(nb_dig(11011, 2))    #  9481
print(nb_dig(12224, 8))    #  7733
print(nb_dig(11549, 1))    #  11905
print(nb_dig(14550, 7))    #  8014
print(nb_dig(8304, 7))     #  3927
print(nb_dig(10576, 9))    #  7860
print(nb_dig(12526, 1))    #  13558
print(nb_dig(7856, 4))     #  7132
print(nb_dig(14956, 1))    #  17267
