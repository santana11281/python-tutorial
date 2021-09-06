class Person:

    def __init__(self):
        self.name = 'Michael'
        self.age = 24
        self.career = 'Prgrammer'

    def language(self):
        return f'{self.name} writes Python'


employee = Person()
print(f'{employee.name} + {employee.age} + {employee.career} + {employee.language()}')
