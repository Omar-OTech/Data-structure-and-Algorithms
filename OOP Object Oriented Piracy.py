class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        
    def is_worth_it(self):
        return self.draft - self.crew * 1.5 > 20
    
titanic = Ship(15, 10)

print(titanic.is_worth_it())    # False
titanic = Ship(15, 10)
print(titanic.draft)    # 15
print(titanic.crew)    # 10
print(titanic.is_worth_it())    # False
titanic = Ship(15, 10)
print(titanic.is_worth_it())    # False
titanic = Ship(15, 10)
