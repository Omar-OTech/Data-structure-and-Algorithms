def partlist(arr):
    res = []
    for i in range(1, len(arr)):
        res.append((" ".join(arr[:i]), " ".join(arr[i:])))
    return res

print(partlist(["I", "wish", "I", "hadn't", "come"]))  # [("I", "wish I hadn't come"), ("I wish", "I hadn't come"), ("I wish I", "hadn't come"), ("I wish I hadn't", "come")]
print(partlist(["cdIw", "tzIy", "xDu", "rThG"]))       # [("cdIw", "tzIy xDu rThG"), ("cdIw tzIy", "xDu rThG"), ("cdIw tzIy xDu", "rThG")]
print(partlist(["vJQ", "anj", "mQDq", "sOZ"]))         # [("vJQ", "anj mQDq sOZ"), ("vJQ anj", "mQDq sOZ"), ("vJQ anj mQDq", "sOZ")]
    