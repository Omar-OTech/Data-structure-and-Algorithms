name_list = ['Abe', 'Bob', 'Chole', 'pop']
score_list = [55, 63, 72, 54]
for i in range(4):
    print(name_list[i], score_list[i])
    
print('=' * 50)
    
name_list = ['Abe', 'Bob', 'Chole', 'pop']
for i, name in enumerate(name_list):
    print(name, 'Has Number', i+1)