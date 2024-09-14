def kebabize(st):
    res = ''
    for i in st:
        if i.isalpha():
            if i.isupper():
                res += '-' + i.lower()
            else:
                res += i.lower()
    return res.strip('-')


print(kebabize('myCamelCasedString'))   # 'my-camel-cased-string'
print(kebabize('myCamelHas3Humps'))     # 'my-camel-has-humps'
print(kebabize('SOS'))                  # 's-o-s'
print(kebabize('42'))                   # ''
print(kebabize('CodeWars'))             # 'code-wars'