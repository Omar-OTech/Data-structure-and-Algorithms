def last(s):
    split_s = s.split()
    return sorted(split_s, key=lambda x: x[-1])

print(last("man i need a taxi up to ubud"))                 # ["a", "need", "ubud", "i", "taxi", "man", "to", "up"])
print(last("what time are we climbing up the volcano"))     # ["time", "are", "we", "the", "climbing", "volcano", "up", "what"]) 
print(last("take me to semynak"))                           # ["take", "me", "semynak", "to"])
print(last("massage yes massage yes massage"))              # ["massage", "massage", "massage", "yes", "yes"])
print(last("take bintang and a dance please"))              # ["a", "and", "take", "dance", "please", "bintang"])