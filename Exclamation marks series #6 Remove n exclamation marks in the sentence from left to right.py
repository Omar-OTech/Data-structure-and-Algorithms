def remove(st, n):
    return st.replace("!", "", n)


print(remove("Hi!",1))                    # "Hi"
print(remove("Hi!",100))                  # "Hi"
print(remove("Hi!!!",1))                  # "Hi!!"
print(remove("Hi!!!",100))                # "Hi"
print(remove("!Hi",1))                    # "Hi"
print(remove("!Hi!",1))                   # "Hi!"
print(remove("!Hi!",100))                 # "Hi"
print(remove("!!!Hi !!hi!!! !hi",1))      # "!!Hi !!hi!!! !hi"
print(remove("!!!Hi !!hi!!! !hi",3))      # "Hi !!hi!!! !hi"
print(remove("!!!Hi !!hi!!! !hi",5))      # "Hi hi!!! !hi"
print(remove("!!!Hi !!hi!!! !hi",100))    # "Hi hi hi"