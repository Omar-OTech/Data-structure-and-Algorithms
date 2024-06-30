def greet(language):

    database = [ ("english", "Welcome")
    , ("czech", "Vitejte")
    , ("danish", "Velkomst")
    , ("dutch", "Welkom")
    , ("estonian", "Tere tulemast")
    , ("finnish", "Tervetuloa")
    , ("flemish", "Welgekomen")
    , ("french", "Bienvenue")
    , ("german", "Willkommen")
    , ("irish", "Failte")
    , ("italian", "Benvenuto")
    , ("latvian", "Gaidits")
    , ("lithuanian", "Laukiamas")
    , ("polish", "Witamy")
    , ("spanish", "Bienvenido")
    , ("swedish", "Valkommen")
    , ("welsh", "Croeso")
    ]

    for k, v in database:
        if k == language:
            return v
    return "Welcome"

print(greet('english'))               # 'Welcome'
print(greet('dutch'))                 # 'Welkom'
print(greet('IP_ADDRESS_INVALID'))    # 'Welcome'
print(greet(''))                      # 'Welcome'
print(greet(2))                       # 'Welcome'