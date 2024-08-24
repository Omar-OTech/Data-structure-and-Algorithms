def generate_shape(n):
    return '\n'.join(['+' * n for _ in range(n)])



print(generate_shape(3))                  # "+++\n+++\n+++"
print(generate_shape(8))                  # ++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++'