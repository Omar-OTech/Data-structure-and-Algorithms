def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""
    res = ""
    for i in range(len(strarr) - k + 1):
        current = "".join(strarr[i: i + k])
        if len(current) > len(res):
            res = current
    return res


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))                                       # "abigailtheta"
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))    # "oocccffuucccjjjkkkjyyyeehh"
print(longest_consec([], 3))                                                                                        # ""
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2))  # "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))                                    # "wlwsasphmxxowiaxujylentrklctozmymu"
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2))                                      # ""
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))                                            # "ixoyx3452zzzzzzzzzzzz"
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15))                                           # ""
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0))                                            # ""