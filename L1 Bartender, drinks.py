def get_drink_by_profession(param):
    param = param.lower()
    drink_dict = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }

    # Return the corresponding value if found, otherwise return "Beer"
    return drink_dict.get(param, "Beer")



print(get_drink_by_profession("jabrOni"))              # "Patron Tequila", "'Jabroni' should map to 'Patron Tequila'"
print(get_drink_by_profession("scHOOl counselor"))     # "Anything with Alcohol", "'School Counselor' should map to 'Anything with alcohol'"
print(get_drink_by_profession("prOgramMer"))           # "Hipster Craft Beer", "'Programmer' should map to 'Hipster Craft Beer'"
print(get_drink_by_profession("bike ganG member"))     # "Moonshine", "'Bike Gang Member' should map to 'Moonshine'"
print(get_drink_by_profession("poLiTiCian"))           # "Your tax dollars", "'Politician' should map to 'Your tax dollars'"
print(get_drink_by_profession("rapper"))               # "Cristal", "'Rapper' should map to 'Cristal'"
print(get_drink_by_profession("pundit"))               # "Beer", "'Pundit' should map to 'Beer'"
print(get_drink_by_profession("Pug"))                  # "Beer", "'Pug' should map to 'Beer'"