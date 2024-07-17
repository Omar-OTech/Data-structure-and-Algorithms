def reverse(st):
# 1st solution
    return ' '.join(st.split()[::-1])

#2nd solution
#     return ' '.join(reversed(st.split()))

print(reverse('Hello World'))   #  'World Hello'
print(reverse('Hi There.'))     #  'There. Hi'