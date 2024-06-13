import math

def find_next_square(sq):
# 1st solution
    root = math.sqrt(sq)
    if root.is_integer():
        return int((root + 1) ** 2)
    return -1

# # 2nd solution
    # root = sq ** 0.5
    # if root.is_integer():
    #     return int((root + 1) ** 2)
    # return -1


print(find_next_square(121))            # 144, "Wrong output for 121"
print(find_next_square(625))            # 676, "Wrong output for 625"
print(find_next_square(319225))         # 320356, "Wrong output for 319225"
print(find_next_square(15241383936))    # 15241630849, "Wrong output for 15241383936"
print(find_next_square(155))            # -1, "Wrong output for 155"
print(find_next_square(342786627))      # -1, "Wrong output for 342786627"