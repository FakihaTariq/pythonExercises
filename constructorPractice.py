class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hi, I am {self.name}')

fakiha = Person("Fakiha Tariq")
print(fakiha.name)
fakiha.talk()

bob = Person("Bob Smith")
bob.talk()