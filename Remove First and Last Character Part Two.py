def array(string):
    return ' '.join(string.split(',')[1:-1]) if len(string.split(',')) > 2 else None



print(array('1,2,3'))         # '2'
print(array('1,2,3,4'))       # '2 3'
print(array('1,2,3,4,5'))     # '2 3 4'
print(array(''))              # None
print(array('1'))             # None
print(array('1,2'))           # None