def friend(x):
    res = []
    for i in range(len(x)):
        if len(x[i]) == 4:
            res.append(x[i])
    return res



print(friend(["Ryan", "Kieran", "Mark",]))                                           # ["Ryan", "Mark"]
print(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]))                             # ["Ryan"]
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))      # ["Jimm", "Cari", "aret"]