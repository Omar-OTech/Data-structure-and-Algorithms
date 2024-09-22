FIRST_NAME = {
    'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', 'D': 'Data', 'E': 'Energy', 
    'F': 'Function', 'G': 'Glitch', 'H': 'Half-life', 'I': 'Ice', 'J': 'Java',
    'K': 'Keystroke', 'L': 'Logic', 'M': 'Malware', 'N': 'Nagware', 'O': 'OS',
    'P': 'Phishing', 'Q': 'Quantum', 'R': 'RAD', 'S': 'Strike', 'T': 'Trojan',
    'U': 'Ultraviolet', 'V': 'Vanilla', 'W': 'WiFi', 'X': 'Xerox', 'Y': 'Y', 'Z': 'Zero'
}

SURNAME = {
    'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst', 'D': 'Discharge', 'E': 'Electron',
    'F': 'Faraday', 'G': 'Gig', 'H': 'Hacker', 'I': 'IP', 'J': 'Jabber',
    'K': 'Killer', 'L': 'Lazer', 'M': 'Mike', 'N': 'n00b', 'O': 'Overclock',
    'P': 'Payload', 'Q': 'Quark', 'R': 'Roy', 'S': 'Spy', 'T': 'T-Rex',
    'U': 'Unit', 'V': 'Virus', 'W': 'Worm', 'X': 'X', 'Y': 'Yob', 'Z': 'Zombie'
}

def alias_gen(f_name, l_name):
    # Check if the first character of both names is an alphabet letter
    if not f_name[0].isalpha() or not l_name[0].isalpha():
        return "Your name must start with a letter from A - Z."
    
    # Convert the first characters to uppercase to match the dictionaries
    first_initial = f_name[0].upper()
    last_initial = l_name[0].upper()
    
    # Get the corresponding alias parts
    first_alias = FIRST_NAME.get(first_initial)
    last_alias = SURNAME.get(last_initial)
    
    # Return the full alias
    return f"{first_alias} {last_alias}"



print(alias_gen('Mike', 'Millington'))                # 'Malware Mike'
print(alias_gen('Fahima', 'Tash'))                    # 'Function T-Rex'
print(alias_gen('Daisy', 'Petrovic'))                 # 'Data Payload'
print(alias_gen('Barny', 'White'))                    # 'Beta Worm'
print(alias_gen('Hank', 'Kutz'))                      # 'Half-life Killer'
print(alias_gen('123abc', 'Pinkman'))                 # 'Your name must start with a letter from A - Z.'
print(alias_gen('walter', 'white'))                   # 'WiFi Worm'