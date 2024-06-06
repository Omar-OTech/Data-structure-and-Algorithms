def duplicate_count(text):
    lower_text = text.lower()
    count = 0
    for i in set(lower_text):
        if lower_text.count(i) > 1:
            count += 1
    return count



print(duplicate_count(""))                          # 0
print(duplicate_count("abcde"))                     # 0
print(duplicate_count("abcdeaa"))                   # 1
print(duplicate_count("abcdeaB"))                   # 2
print(duplicate_count("Indivisibilities"))          # 2