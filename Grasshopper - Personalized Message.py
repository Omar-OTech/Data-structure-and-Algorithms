def greet(name, owner):
    return 'Hello boss' if name == owner else "Hello guest"


print(greet('Daniel', 'Daniel'))    # 'Hello boss'
print(greet('Greg', 'Daniel'))      # 'Hello guest'