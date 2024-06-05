def get_count(sentence):
# 1st solution
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in sentence:
        if i in vowel:
            count += 1
    return count

# 2nd solution
    # return sum(1 for i in sentence if i in "aeiou")



print(get_count("aeiou"))
print(get_count("y"))
print(get_count("bcdfghjklmnpqrstvwxz y"))
print(get_count(""))
print(get_count("abracadabra"))