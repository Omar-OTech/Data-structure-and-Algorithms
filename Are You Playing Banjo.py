def are_you_playing_banjo(name):
# 1st solution
    if name[0] == "R" or name[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

# 2nd solution
    # if name.startswith('R') or name.startswith('r'):
    #     return name + ' plays banjo'
    # else:
    #     return name + ' does not play banjo'

print(are_you_playing_banjo("martin"))  # "martin does not play banjo"
print(are_you_playing_banjo("Rikke"))   # "Rikke plays banjo"
print(are_you_playing_banjo("bravo"))   # "bravo does not play banjo"
print(are_you_playing_banjo("rolf"))    # "rolf plays banjo"
