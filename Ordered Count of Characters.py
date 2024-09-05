def ordered_count(inp):
# 1st solution
    return [(i, inp.count(i)) for i in sorted(set(inp), key=inp.index)]


print(ordered_count('abracadabra'))  #  [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)])
print(ordered_count('Code Wars'))    #  [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])