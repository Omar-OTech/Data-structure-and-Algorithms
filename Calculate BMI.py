def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5: return "Underweight"
    elif bmi <= 25.0: return "Normal"
    elif bmi <= 30.0: return "Overweight"
    elif bmi > 30: return "Obese"


print(bmi(50, 1.80))   # "Underweight"
print(bmi(80, 1.80))   # "Normal"
print(bmi(90, 1.80))   # "Overweight"
print(bmi(110, 1.80))  # "Obese"
print(bmi(50, 1.50))   # "Normal"