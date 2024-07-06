def rental_car_cost(d):
# 1st solution
    if d < 3:
        return d * 40 # 1 to 2 days
    elif d < 7:
        return d * 40 - 20 # 3 to 6 days
    return d * 40 - 50  # 7 days or more

# 2nd solution
    # if d < 3:
    #     return d * 40
    # elif d >= 3 and d < 6:
    #     return ( d * 40 ) - 20
    # elif d >= 7:
    #     return ( d * 40 ) - 50

print(rental_car_cost(1))     #  40
print(rental_car_cost(4))     #  140
print(rental_car_cost(7))     #  230
print(rental_car_cost(8))     #  270