def uefa_euro_2016(teams, scores):
    res = "At match " + teams[0] + " - " + teams[1] + ", "
    if scores[0] > scores[1]:
        return res + teams[0] + " won!"
    elif scores[0] < scores[1]:
        return res + teams[1] + " won!"
    else:
        return res + "teams played draw."


print(uefa_euro_2016(['Germany', 'Ukraine'], [2, 0]))                 # "At match Germany - Ukraine, Germany won!");
print(uefa_euro_2016(['Belgium', 'Italy'], [0, 2]))                   # "At match Belgium - Italy, Italy won!")
print(uefa_euro_2016(['Portugal', 'Iceland'], [1, 1]))                # "At match Portugal - Iceland, teams played draw.")
print(uefa_euro_2016(['Albania', 'Switzerland'], [1, 2]))             # "At match Albania - Switzerland, Switzerland won!")
print(uefa_euro_2016(['Republic of Ireland', 'Sweden'], [0, 0]))      # "At match Republic of Ireland - Sweden, teams played draw.")
