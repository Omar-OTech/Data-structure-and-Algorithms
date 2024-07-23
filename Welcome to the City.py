def say_hello(name, city, state):
    name = ' '.join(name)
    return f"Hello, {name}! Welcome to {city}, {state}!"

# return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"

print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))                    # 'Hello, John Smith! Welcome to Phoenix, Arizona!')
print(say_hello(['Franklin','Delano','Roosevelt'], 'Chicago', 'Illinois'))   # 'Hello, Franklin Delano Roosevelt! Welcome to Chicago, Illinois!')
print(say_hello(['Wallace','Russel','Osbourne'],'Albany','New York'))        # 'Hello, Wallace Russel Osbourne! Welcome to Albany, New York!')
print(say_hello(['Lupin','the','Third'],'Los Angeles','California'))         # 'Hello, Lupin the Third! Welcome to Los Angeles, California!')
print(say_hello(['Marlo','Stanfield'],'Baltimore','Maryland'))               # 'Hello, Marlo Stanfield! Welcome to Baltimore, Maryland!')