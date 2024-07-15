def name_shuffler(str_):
# 1st solution
    return str_.split()[1] + ' ' + str_.split()[0]

# 2nd solution
    # return ' '.join(str_.split()[::-1])

# 3rd solution
    # return ' '.join(reversed(str_.split()))

print(name_shuffler('john McClane'))          # 'McClane john'
print(name_shuffler('Mary jeggins'))          # 'jeggins Mary'
print(name_shuffler('tom jerry'))             # 'jerry tom')