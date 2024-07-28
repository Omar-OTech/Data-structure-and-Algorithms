def rain_amount(mm):
    if mm >= 40:
        return "Your plant has had more than enough water for today!"
    else:
        return f"You need to give your plant {40 - mm}mm of water"


print(rain_amount(100))  # "Your plant has had more than enough water for today!"
print(rain_amount(40))   # "Your plant has had more than enough water for today!"
print(rain_amount(39))   # "You need to give your plant 1mm of water"
print(rain_amount(5))    # "You need to give your plant 35mm of water"
print(rain_amount(0))    # "You need to give your plant 40mm of water"