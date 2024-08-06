def calculate_age(year_of_birth, current_year):
    if year_of_birth == current_year:
        return "You were born this very year!"
    elif year_of_birth < current_year:
        age = current_year - year_of_birth
        if age == 1:
            return f"You are {age} year old."
        return f"You are {age} years old."
    else:
        age = year_of_birth - current_year
        if age == 1:
            return f"You will be born in {age} year."
        return f"You will be born in {age} years."

print(calculate_age(2012, 2016))         #"You are 4 years old.")
print(calculate_age(1989, 2016))         #"You are 27 years old.")
print(calculate_age(2000, 2090))         #"You are 90 years old.")
print(calculate_age(2000, 1990))         #"You will be born in 10 years.")
print(calculate_age(2000, 2000))         #"You were born this very year!")
print(calculate_age(900, 2900))          #"You are 2000 years old.")
print(calculate_age(2010, 1990))         #"You will be born in 20 years.")
print(calculate_age(2010, 1500))         #"You will be born in 510 years.")
print(calculate_age(2011, 2012))         #"You are 1 year old.")
print(calculate_age(2000, 1999))         #"You will be born in 1 year.")