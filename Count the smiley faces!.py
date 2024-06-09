def count_smileys(arr):
# 1st solution
    valid = [":)", ";)", ":D", ";D", ";-D", ":-D", ":~D", ";~D", ":-)", ";-)", ";~)", ":~)"]
    res = 0
    for i in arr:
        if i in valid:
            res += 1
    return res

# 2nd solution
    # eyes = [":", ";"]
    # noses = ["", "-", "~"]
    # mouths = [")", "D"]
    # res = 0
    # for eye in eyes:
    #     for nose in noses:
    #         for mouth in mouths:
    #             face = eye + nose + mouth
    #             res += arr.count(face)
    # return res




print(count_smileys([]))                                        # 0
print(count_smileys([':D',':~)',';~D',':)']))                   # 4
print(count_smileys([':)',':(',':D',':O',':;']))                # 2
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))           # 1