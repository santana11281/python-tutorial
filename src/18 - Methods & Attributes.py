class Person:
    isAlive = 'yes'

    def __init__(self, name, age, career):
        self.name = name
        self.age = age
        self.career = career

    def whatIDo(self):
        if (self.age > 1):
            return f'My name is {self.name}, i am {self.age} years old and i am a  {self.career}'
        else:
            return f'My name is {self.name}, i am {self.age} year old and i am a  {self.career}'

    # new
    @classmethod
    def sayHi(cls):
        return "'Hi world'"

    # new
    @staticmethod
    def spin (speed="too fast"):
        return f'the planet is {speed}'


# ambar = Person("Ambar Santana", 13, "Danzarina")
# michael = Person("Michael Santana", 24, "Programmer")
# netnija = Person("Ninja", 1, "Developer")

# print(f"{netnija.whatIDo()} ")

# new
print(f"and is alive? {Person.isAlive} and says {Person.sayHi()}")
print(Person.spin("too slow"))
