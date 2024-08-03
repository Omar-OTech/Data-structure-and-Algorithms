def derive(coefficient, exponent):
    return f"{coefficient * exponent}x^{exponent - 1}"


print(derive(7,8))  # 56x^7
print(derive(5,9))  # 45x^8