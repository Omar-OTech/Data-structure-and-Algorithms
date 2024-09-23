def calculate(num1, operation, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Check for division by zero
        if num2 == 0:
            return None
        return num1 / num2
    else:
        # Unsupported operation
        return None

    

print(calculate(3.2,"+", 8))     # 11.2, "3.2 + 8 = 11.2"
print(calculate(3.2,"-", 8))     # -4.8, "3.2 - 8 = -4.8"
print(calculate(3.2,"/", 8))     # 0.4, "3.2 / 8 = .4"
print(calculate(3.2,"*", 8))     # 25.6, "3.2 * 8 = 25.6"
print(calculate(-3,"+", 0))      # -3, "-3 + 0 = -3"
print(calculate(-3,"-", 0))      # -3, "-3 - 0 = -3"
print(calculate(-2, "/", -2))    # 1, "-2 / -2 = 1"
print(calculate(-3,"*", 0))      # 0, "-3 * 0 = 0"