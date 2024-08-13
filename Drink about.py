def people_with_age_drink(age):
# 1st solution
    if age < 14:
        return 'drink toddy'
    elif age >= 14 and age < 18:
        return 'drink coke'
    elif age >= 18 and age < 21:
        return 'drink beer'
    elif age >= 21:
        return 'drink whisky'

# 2nd solution
    # if age > 20: return 'drink whisky'
    # if age > 17: return 'drink beer'
    # if age > 13: return 'drink coke'
    # return 'drink toddy'

print(people_with_age_drink(13))     # 'drink toddy', "Wrong result for 13")
print(people_with_age_drink(0))      # 'drink toddy', "Wrong result for 0")
print(people_with_age_drink(17))     # 'drink coke')
print(people_with_age_drink(15))     # 'drink coke')
print(people_with_age_drink(14))     # 'drink coke')
print(people_with_age_drink(20))     # 'drink beer')
print(people_with_age_drink(18))     # 'drink beer')
print(people_with_age_drink(22))     # 'drink whisky')
print(people_with_age_drink(21))     # 'drink whisky')