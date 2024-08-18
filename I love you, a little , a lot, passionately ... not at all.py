def how_much_i_love_you(nb_petals):
# 1st solution
    if nb_petals % 6 == 1:
        return "I love you"
    elif nb_petals % 6 == 2:
        return "a little"
    elif nb_petals % 6 == 3:
        return "a lot"
    elif nb_petals % 6 == 4:
        return "passionately"
    elif nb_petals % 6 == 5:
        return 'madly'
    elif nb_petals % 6 == 0:
        return "not at all"

# 2nd solution
    # return ['not at all', 'I love you', 'a little', 'a lot', 'passionately', 'madly'][nb_petals % 6]

print(how_much_i_love_you(7))      #"I love you"
print(how_much_i_love_you(3))      #"a lot"
print(how_much_i_love_you(6))      #"not at all"