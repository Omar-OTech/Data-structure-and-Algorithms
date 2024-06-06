def string_to_array(s):
    res = []
    split = s.split(" ")
    for i in split:
        res.append(i)
    return res



print(string_to_array("Robin Singh"))                                     # ["Robin", "Singh"]
print(string_to_array("CodeWars"))                                        # ["CodeWars"]
print(string_to_array("I love arrays they are my favorite"))              # ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(string_to_array("1 2 3"))                                           # ["1", "2", "3"]
print(string_to_array(""))                                                # [""]