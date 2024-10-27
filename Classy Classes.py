class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"

# 2nd solution
        # self.name = name
        # self.age = age
        # @property
        # def info(self):
        #     return f"{self.name}s age is {self.age}"


# test code
person1 = Person('John', 25)
print(person1.info.format(name='John', age=25))

person2 = Person('Kim', 22)
print(person2.info.format(name='Kim', age=25))

person3 = Person('Alice', 24)
print(person3.info.format(name='Alice', age=25))

person4 = Person('Bob', 32)
print(person4.info.format(name='Bob', age=25))