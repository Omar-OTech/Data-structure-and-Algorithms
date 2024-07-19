def position(alphabet):
# 1st solution
    dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 
    14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
    
    for i in dict:
        if dict[i] == alphabet:
            return f"Position of alphabet: {i}"
        
# 2nd solution
    # return f"Position of alphabet: {ord(alphabet) - 96}"
    
print(position('a'))  # "Position of alphabet: 1"
print(position('z'))  # "Position of alphabet: 26"
print(position('e'))  # "Position of alphabet: 5"
print(position('b'))  # "Position of alphabet: 2"
print(position('d'))  # "Position of alphabet: 4"
print(position('x'))  # "Position of alphabet: 24"
print(position('h'))  # "Position of alphabet: 8"