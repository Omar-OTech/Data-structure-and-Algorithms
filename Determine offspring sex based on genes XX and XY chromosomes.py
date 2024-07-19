def chromosome_check(chromosome):
    female = 'XX'
    if chromosome.upper() == female:
        return 'Congratulations! You\'re going to have a daughter.'
    else:
        return 'Congratulations! You\'re going to have a son.'

# 2nd solution
# return f"Congratulations! You're going to have a {'son' if 'Y' in chromosome else 'daughter'}."

print(chromosome_check('XY'))   # 'Congratulations! You\'re going to have a son.')
print(chromosome_check('XX'))   # 'Congratulations! You\'re going to have a daughter.')