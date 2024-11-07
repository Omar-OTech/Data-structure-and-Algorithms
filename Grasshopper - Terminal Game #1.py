class Hero(object):
    def __init__(self, name="Hero", position="00", health=100, damage=5, experience=0):
        self.name = name
        self.position = position
        self.health = health
        self.damage = damage
        self.experience = experience

    def __str__(self):
        return "Name: {}, Position: {}, Health: {}, Damage: {}, Experience: {}".format(self.name, self.position, self.health, self.damage, self.experience)


# 2nd solution
    #     self._name = name
    #     self._experience = 0
    #     self._health = 100
    #     self._position = '00'
    #     self._damage = 5
    
    # @property
    # def name(self):
    #     return self._name
    
    # @property
    # def experience(self):
    #     return self._experience

    # @property
    # def health(self):
    #     return self._health
    
    # @property
    # def position(self):
    #     return self._position
    
    @property
    def damage(self):
        return self._damage

myHero = Hero()
print(myHero.name)          # 'Hero'
print(myHero.experience)    # 0
print(myHero.health)        # 100
print(myHero.position)      # '00'
print(myHero.damage)        # 5