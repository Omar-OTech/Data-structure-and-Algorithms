def correct_polish_letters(st):
    dict = {'ą' : 'a', 'ć' : 'c', 'ę' : 'e', 'ł' : 'l', 'ń' : 'n', 'ó' : 'o', 'ś' : 's', 'ź' : 'z', 'ż' : 'z'}
    for k, v in dict.items():
        st = st.replace(k, v)
    return st

print(correct_polish_letters("Jędrzej Błądziński"))         # "Jedrzej Bladzinski"
print(correct_polish_letters("Lech Wałęsa"))                # "Lech Walesa"
print(correct_polish_letters("Maria Skłodowska-Curie"))     # "Maria Sklodowska-Curie"