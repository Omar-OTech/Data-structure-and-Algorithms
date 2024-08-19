websites = ['codewars'] * 1000

# websites = ['codewars' for _ in range(1000)]



print(len(websites))           # 1000
print(type(websites))          # list
print(list(set(websites)))     # ["codewars"]