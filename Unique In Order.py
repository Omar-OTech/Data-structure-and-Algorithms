def unique_in_order(sequence):
    if sequence == "":
        return []
    elif sequence == [] or sequence == ():
        return []
    else:
        if isinstance(sequence, str):
            sequence = list(sequence)
        elif isinstance(sequence, tuple):
            sequence = list(sequence)
        res = [sequence[0]]
        for i in range(1, len(sequence)):
            if sequence[i] != sequence[i-1]:
                res.append(sequence[i])
        return res


print(unique_in_order(""))                          # []
print(unique_in_order([]))                          # []
print(unique_in_order(()))                          # []
print(unique_in_order("A"))                         # ["A"]
print(unique_in_order(["A"]))                       # ["A"]
print(unique_in_order(("A",)))                      # ["A"]
print(unique_in_order("AA"))                        # ["A"]
print(unique_in_order("AAAABBBCCDAABBB"))           # ["A", "B", "C", "D", "A", "B"]
print(unique_in_order("ABBCcA"))                    # ["A", "B", "C", "c", "A"]
print(unique_in_order([1, 2, 3, 3, -1]))            # [1, 2, 3, -1]
print(unique_in_order(["a", "b", "b", "a"]))        # ["a", "b", "a"]