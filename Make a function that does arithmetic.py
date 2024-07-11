def arithmetic(a, b, operator):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        return a / ( b * 1.0)
    if operator == "add":
        return add(a, b)
    if operator == "subtract":
        return subtract(a, b)
    if operator == "multiply":
        return multiply(a, b)
    if operator == "divide":
        return divide(a, b)

# 2nd solution
    # return {
    #         'add': a + b,
    #         'subtract': a - b,
    #         'multiply': a * b,
    #         'divide': a / b,
    # } [operator]

# 3rd solution
    # if operator == 'add':
    #     return a + b
    # elif operator == 'subtract':
    #     return a - b
    # elif operator == 'multiply':
    #     return a * b
    # elif operator == 'divide':
    #     return a / b

print(arithmetic(1, 2, "add"))       #  3, "'add' should return the two numbers added together!"
print(arithmetic(8, 2, "subtract"))  #  6, "'subtract' should return a minus b!"
print(arithmetic(5, 2, "multiply"))  #  10, "'multiply' should return a multiplied by b!"
print(arithmetic(8, 2, "divide"))    #  4, "'divide' should return a divided by b!"
