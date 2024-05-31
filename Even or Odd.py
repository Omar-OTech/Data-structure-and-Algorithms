# Odd numbers are those numbers that cannot be divided into two equal parts
# Even numbers are those numbers that can be divided into two equal parts

def even_or_odd(number):
# 1st solution
    if number % 2 == 0:
        return 'Even'
    else:
        return "Odd"

# 2nd solution
    # return 'Even' if number % 2 == 0 else 'Odd'

# 3rd solution
    # return['Even', 'Odd'] [number % 2]







print(even_or_odd(1))  # "Odd"
print(even_or_odd(2))  # "Even"
print(even_or_odd(-1)) # "Odd"        
print(even_or_odd(-2)) # "Even"
print(even_or_odd(0))  # "Even"