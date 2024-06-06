def zero_fuel(distance_to_pump, mpg, fuel_left):
# 1st solution
    max_distance = mpg * fuel_left
    if max_distance >= distance_to_pump:
        return True
    else:
        return False
# 2nd solution
    # return distance_to_pump <= mpg * fuel_left


print(zero_fuel(50, 25, 2)) # True
print(zero_fuel(100, 50, 1)) # False