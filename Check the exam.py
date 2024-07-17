def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        if arr2[i] == "":
            score += 0
        elif arr1[i] == arr2[i]:
            score += 4
        else:
            score -= 1
    return score if score > 0 else 0


print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))  #  6
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]))  #  7
print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]))  #  16
print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]))  #  0