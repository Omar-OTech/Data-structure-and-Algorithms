def make_string(s):
    res = ""
    for i in s.split():
        res += i[0]
    return res

# 2nd solution
    # return ''.join([i[0] for i in s.split()])


print(make_string("sees nose xray yoat"))            #"snxy", "Wrong result for 'sees eyes xray yoat'"
print(make_string("brown eyes are nice"))            #"bean", "Wrong result for 'brown eyes are nice'"
print(make_string("cars are very nice"))             #"cavn", "Wrong result for 'cars are very nice'"
print(make_string("kaks de gan has a big head"))     #"kdghabh", "Wrong result for 'kaks de gan has a big head'"