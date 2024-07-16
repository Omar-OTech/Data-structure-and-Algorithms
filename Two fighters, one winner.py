def declare_winner(fighter1, fighter2, first_attacker):
    fighter1_damage_per_attack = fighter1[2]
    fighter2_damage_per_attack = fighter2[2]
    fighter1_health = fighter1[1]
    fighter2_health = fighter2[1]
    
    while fighter1_health > 0 and fighter2_health > 0:
        if first_attacker == fighter1[0]:
            fighter2_health -= fighter1_damage_per_attack
            if fighter2_health <= 0:
                return fighter1[0]
            fighter1_health -= fighter2_damage_per_attack
            if fighter1_health <= 0:
                return fighter2[0]
        else:
            fighter1_health -= fighter2_damage_per_attack
            if fighter1_health <= 0:
                return fighter2[0]
            fighter2_health -= fighter1_damage_per_attack
            if fighter2_health <= 0:
                return fighter1[0]



print(declare_winner(("Lew", 10, 2), ("Harry", 5, 4), "Lew"))          #  "Lew"
print(declare_winner(("Lew", 10, 2), ("Harry", 5, 4), "Harry"))        # "Harry"
print(declare_winner(("Harald", 20, 5), ("Harry", 5, 4), "Harry"))     # "Harald"
print(declare_winner(("Harald", 20, 5),("Harry", 5, 4), "Harald"))     # "Harald"
print(declare_winner(("Jerry", 30, 3), ("Harald", 20, 5), "Jerry"))    #  "Harald"
print(declare_winner(("Jerry", 30, 3), ("Harald", 20, 5), "Harald"))   # "Harald"




class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
    
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__